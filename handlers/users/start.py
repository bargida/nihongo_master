from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.startMenuKeyboard import menuStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.full_name}!", reply_markup=menuStart)
