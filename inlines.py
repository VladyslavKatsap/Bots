from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

with open("Groups/302.txt", "r", encoding="utf-8") as f:
    lines = f.read()

ikb_menu = InlineKeyboardMarkup(row_width=2,
                                inline_keboard=[
                                    [
                                        InlineKeyboardButton(text='Понеділок',callback_data=lines)
                                    ]
                                ] )