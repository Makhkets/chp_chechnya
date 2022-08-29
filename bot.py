from pprint import pprint
from loguru import logger as l

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import Message

import json
from time import sleep

storage = MemoryStorage()
bot = Bot(token="502296: DELETED  3ko2PiQhd3E", parse_mode='html')
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=["start"])
async def start(message: Message):

    while True:
        with open("channel_messages.json", "r", encoding="utf-8") as file:
            data = json.load(file)

            for string in data:
                # if type(string.get("message")) is None:
                #     pass

                l.success(type(string.get("message")))


        await message.answer('Успешно закончил свою работу')
        sleep(120)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)