import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hlink, link
from dataclasses import dataclass
import os
from aiogram.dispatcher.filters import Text
import btns as kb
import datetime


@dataclass(frozen=True)
class Messages:
    test: str = "{name},"


msg = Messages()

bot = Bot(token="")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

code_to_group = {
    '101': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\101.txt",
    '102': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\102.txt",
    '103': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\103.txt",
    '104': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\104.txt",
    '105': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\105.txt",
    '106': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\106.txt",
    '107': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\107.txt",
    '113': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\113.txt",
    '114': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\114.txt",
    '116': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\116.txt",
    '117': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\117.txt",
    # ----------------------------------------------------------------
    '201': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\201.txt",
    '202': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\202.txt",
    '203': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\203.txt",
    '204': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\204.txt",
    '205': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\205.txt",
    '206': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\206.txt",
    '207': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\207.txt",
    '213': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\213.txt",
    '214': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\214.txt",
    '216': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\216.txt",
    '217': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\217.txt",
    '227': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\227.txt",
    # ----------------------------------------------------------------
    '301': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\301.txt",
    '302': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\302.txt",
    '303': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\303.txt",
    '304': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\304.txt",
    '305': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\305.txt",
    '306': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\306.txt",
    '307': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\307.txt",
    '313': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\313.txt",
    '314': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\314.txt",
    '316': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\316.txt",
    '317': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\317.txt",
    # ----------------------------------------------------------------
    '402': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\402.txt",
    '403': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\403.txt",
    '404': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\404.txt",
    '407': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\407.txt",
    '413': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\413.txt",
    '414': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\414.txt",
    '417': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\417.txt",
    '427': r"C:\Users\Vladyslav\Documents\GitHub\Bots\Groups\427.txt",
}

code_to_smile = {
    1: "\U0001f1fa\U0001f1e6",
    2: "\U0001f602",
    3: "\U0001f609",
    4: "\U0001f914",
    5: "\U0001f447"
}


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    user_name = message.from_user.first_name
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Розклад', 'Дізнатися який зараз тиждень']
    keyboard.add(*buttons)
    await message.reply(f"{msg.test.format(name=user_name)}привіт{code_to_smile[1]}", reply_markup=keyboard)

@dp.message_handler(commands="help")
async def any_text_message2(message: types.Message):
    await message.answer(
        '\n[Написати розробнику](https://t.me/VladyslaV_KP)',
        parse_mode='Markdown')


@dp.message_handler(commands="support")
async def any_text_message2(message: types.Message):
    await message.answer(
        '\n[Допомогти Україні](https://bank.gov.ua/ua/about/support-the-armed-forces)',
        parse_mode='Markdown')


list_hi = ['привіт', 'здоров', 'хелоу', 'салют', 'добрий день']
list_txt = ['Розклад']

@dp.message_handler(Text(equals="Дізнатися який зараз тиждень"))
async def with_p(message: types.Message):
    week_number = datetime.datetime.today().isocalendar()[1]
    if week_number%2 != 0:
        await message.reply("Зараз 1-й тиждень")
    else:
        await message.reply("Зараз 2-й тиждень")

@dp.message_handler(Text(equals="Розклад"))
async def with_p(message: types.Message):
    await message.reply("Ок, введіть групу" + code_to_smile[5])

    @dp.message_handler()
    async def any_text_message1(message: types.Message):
        k1 = message.text
        if k1 in code_to_group:
            with open(code_to_group[k1], "r", encoding="utf-8") as f:
                lines = f.read()
            await message.answer(
                'Розклад для ' + k1 + ' групи\n' + lines + '\n[Розклад на сайті](https://sites.google.com/chnu.edu.ua/natural-department-college/розклад?authuser=1)',
                parse_mode='Markdown')
        elif k1.lower() in list_hi:
            await message.reply("Привіт" + code_to_smile[3])
        elif k1.isdigit() == True and k1 not in code_to_group:
            await message.reply("Такої групи в коледжі нема" + code_to_smile[2])
        elif k1 not in list_txt:
            await message.answer("Навіщо таке писати?" + code_to_smile[4])


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
