import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
from dataclasses import dataclass

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@dataclass(frozen=True)
class Messages:
    test: str = "{name},"


msg = Messages()

bot = Bot(token="No")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

code_to_group = {
    "302": "302.txt"
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
    if k1 == '302':
        await message.answer("Вивести ввесь розклад?")
        k2 = message.text
        if k2 == 'Так' or 'так' or 'Да' or 'да' or 'Yes' or 'yes':
            with open("302.txt", "r", encoding="utf-8") as f:
                lines = f.read()
            await message.answer(lines)
        elif k2 == 'Ні':
            await message.answer("Окремого поки нема")
    elif k1 != '302':
        await message.reply("Поки немає")


# dp.register_message_handler(cmd_start, commands="start")
@dp.message_handler(commands="block")
async def cmd_block(message: types.Message):
    await asyncio.sleep(5.0)
    await message.reply("Ви заблоковані")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
