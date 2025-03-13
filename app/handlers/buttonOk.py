from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboardForOk = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(
        text='OK', callback_data='OK')]
    ])
