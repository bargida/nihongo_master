from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(commands="info_markdown")
async def bot_info(message: types.Message):
    text = f"Assalom alekum, {message.from_user.full_name}\!n"
    text += "Welcome <b>Japanese course </b>"

    await message.answer(text, parse_mode=types.ParseMode.MARKDOWN_V2)