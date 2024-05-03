import asyncio
import logging

import cv2
import numpy as np

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile, InputFile

logging.basicConfig(level=logging.INFO)
bot = Bot(#TOKEN)
dp = Dispatcher()

file_ids = []


@dp.message(Command("start"))
async def cmd_start(message: types.Message):

    await message.answer("Привет, я бот, который умеет обрабатывать изображение :) "
                         "Отправляй фотографию и я её обработаю!")


@dp.message(F.photo)
async def download_photo(message: types.Message, bot: Bot):
    kb = [
        [types.KeyboardButton(text="Черно белое")],
        [types.KeyboardButton(text="Блюр")],
        [types.KeyboardButton(text="Гаус")],
        [types.KeyboardButton(text="Резкость")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите фильтр обработки")
    await message.answer("Какой фильтр будем применять?", reply_markup=keyboard)

    await bot.download(
        message.photo[-1],
        destination=f"downloads\\{message.photo[-1].file_id}.jpg"
    )
    file_ids.append(message.photo[-1].file_id)



@dp.message(F.text.lower() == "черно белое")
async def create_image(message: types.Message):


    new_img = cv2.imread("downloads\\{}.jpg".format(file_ids[0]))

    final_wide = 800
    r = float(final_wide) / new_img.shape[1]
    d = (final_wide, int(new_img.shape[0] * r))

    resized_photo = cv2.resize(new_img, d, interpolation=cv2.INTER_AREA)
    gray_photo = cv2.cvtColor(resized_photo, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f"downloads\\image2.jpg", gray_photo)




    await message.answer_photo(photo=types.FSInputFile
    ("downloads\\image2.jpg"))


@dp.message(F.text.lower() == "блюр")
async def create_image(message: types.Message):
    new_img = cv2.imread("downloads\\{}.jpg".format(file_ids[0]))

    final_wide = 800
    r = float(final_wide) / new_img.shape[1]
    d = (final_wide, int(new_img.shape[0] * r))

    resized_photo = cv2.resize(new_img, d, interpolation=cv2.INTER_AREA)
    av_photo = cv2.blur(resized_photo, (5,5))
    cv2.imwrite(f"downloads\\image3.jpg", av_photo)

    await message.answer_photo(photo=types.FSInputFile
    ("downloads\\image3.jpg"))



@dp.message(F.text.lower() == "гаус")
async def create_image(message: types.Message):
    new_img = cv2.imread("downloads\\{}.jpg".format(file_ids[0]))

    final_wide = 800
    r = float(final_wide) / new_img.shape[1]
    d = (final_wide, int(new_img.shape[0] * r))

    resized_photo = cv2.resize(new_img, d, interpolation=cv2.INTER_AREA)
    gaussian_photo = cv2.GaussianBlur(resized_photo, (5,5), 0)


    cv2.imwrite(f"downloads\\image4.jpg", gaussian_photo)

    await message.answer_photo(photo=types.FSInputFile
    ("downloads\\image4.jpg"))



@dp.message(F.text.lower() == "резкость")
async def create_image(message: types.Message):
    new_img = cv2.imread("downloads\\{}.jpg".format(file_ids[0]))

    final_wide = 800
    r = float(final_wide) / new_img.shape[1]
    d = (final_wide, int(new_img.shape[0] * r))
    resized_photo = cv2.resize(new_img, d, interpolation=cv2.INTER_AREA)

    gaussian_photo = cv2.GaussianBlur(resized_photo, (5, 5), 0)

    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    rez_g_photo = cv2.filter2D(gaussian_photo, -1, kernel)

    cv2.imwrite(f"downloads\\image5.jpg", rez_g_photo)

    await message.answer_photo(photo=types.FSInputFile
    ("downloads\\image5.jpg"))



async def main():
    await dp.start_polling(bot)

if __name__== "__main__":
    asyncio.run(main())




# @dp.message(Command('images'))
# async def upload_photo(message: types.Message):
#     # Сюда будем помещать file_id отправленных файлов, чтобы потом ими воспользоваться
#     file_ids = []
#
#     # Чтобы продемонстрировать BufferedInputFile, воспользуемся "классическим"
#     # открытием файла через `open()`. Но, вообще говоря, этот способ
#     # лучше всего подходит для отправки байтов из оперативной памяти
#     # после проведения каких-либо манипуляций, например, редактированием через Pillow
#     with open("image.jpg", "rb") as image_from_buffer:
#         result = await message.answer_photo(
#             BufferedInputFile(
#                 image_from_buffer.read(),
#                 filename="image.jpg"
#             ),
#             caption="Изображение из буфера"
#         )
#         file_ids.append(result.photo[-1].file_id)






