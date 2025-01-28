from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📚Books"),
            KeyboardButton(text="�Search"),
        ]
    ],
    resize_keyboard=True,

)