import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
from dataclasses import dataclass

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@dataclass(frozen=True)
class Messages:
    test: str = "{name},"


msg = Messages()

bot = Bot(token="5353285649:AAGrdmdj0HR7Yi0wNxmjtPfBghf9yyM1xw0")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

code_to_group = {
    '302': "302.txt",
    '301': "301.txt"
}

code_to_smile = {
    1: "Слава Україні \U0001f1fa\U0001f1e6"
}


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    user_name = message.from_user.first_name
    await message.answer(f"{msg.test.format(name=user_name)}{code_to_smile[1]}\nНапишіть номер групи")


@dp.message_handler()
async def any_text_message1(message: types.Message):
    k1 = message.text
    if k1 in code_to_group:
        with open(code_to_group[k1], "r", encoding="utf-8") as f:
            lines = f.read()
        await message.answer(lines)
    else:
        await message.reply("В розробці...")


# dp.register_message_handler(cmd_start, commands="start")
@dp.message_handler(commands="block")
async def cmd_block(message: types.Message):
    await asyncio.sleep(5.0)
    await message.reply("Ви заблоковані")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
