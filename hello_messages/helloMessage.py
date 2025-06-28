from aiogram import Router
from aiogram.filters.command import Command
from aiogram import types, F, Bot
from funcImage.funcImage import resized_photo, downLoadsImage
from lexicon.lexicon import lexicon_bot
from filterImage.filterImage import grayPhoto, blurPhoto, gausPhoto, sharpNessPhoto



router_image = Router()
file_ids = []

@router_image.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(lexicon_bot["hello"])

@router_image.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(lexicon_bot["help"])

@router_image.message(F.photo)
async def download_photo(message: types.Message, bot: Bot):
    kb = [
        [types.KeyboardButton(text="Черно-белое")],
        [types.KeyboardButton(text="Блюр")],
        [types.KeyboardButton(text="Гаус")],
        [types.KeyboardButton(text="Резкость")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите фильтр обработки")
    await message.answer(lexicon_bot["choose_filter"], reply_markup=keyboard)
    await bot.download(
        message.photo[-1],
        destination=f"downloads\\{message.photo[-1].file_id}.jpg"
    )
    file_ids.append(message.photo[-1].file_id)

@router_image.message(F.text.lower() == "черно-белое")
async def create_image(message: types.Message):
    image = downLoadsImage(file_ids)
    res_photo = resized_photo(image)
    grayPhoto(res_photo)
    await message.answer_photo(photo=types.FSInputFile
    ("downloads\\gray.jpg"))

@router_image.message(F.text.lower() == "блюр")
async def create_image(message: types.Message):
    image = downLoadsImage(file_ids)
    res_photo = resized_photo(image)
    blurPhoto(res_photo)
    await message.answer_photo(photo=types.FSInputFile
    ("downloads\\blur.jpg"))

@router_image.message(F.text.lower() == "гаус")
async def create_image(message: types.Message):
    image = downLoadsImage(file_ids)
    res_photo = resized_photo(image)
    gausPhoto(res_photo)
    await message.answer_photo(photo=types.FSInputFile
    ("downloads\\gaus.jpg"))

@router_image.message(F.text.lower() == "резкость")
async def create_image(message: types.Message):
    image = downLoadsImage(file_ids)
    res_photo = resized_photo(image)
    sharpNessPhoto(res_photo)
    await message.answer_photo(photo=types.FSInputFile
    ("downloads\\sharpNess.jpg"))
