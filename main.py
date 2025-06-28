import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import TOKEN
from hello_messages.helloMessage import router_image

logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN)
dp = Dispatcher()
dp.include_router(router_image)

async def main():
    await dp.start_polling(bot)

if __name__== "__main__":
    asyncio.run(main())










