import asyncio
from environs import Env
from aiogram import Bot, Dispatcher
import logging
from app.handlers import router

env = Env()
env.read_env()

bot = Bot(token=env.str('Api_Token'))
dp = Dispatcher()


async def main():
    dp.include_router(router.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
