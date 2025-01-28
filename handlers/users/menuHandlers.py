import logging

from aiogram.types import Message, CallbackQuery
from aiogram.utils import callback_data

from keyboards.inline.booksKeyboard import categoryMenu, levelsMenu, booksMenu
from keyboards.inline.callbackData import course_callback, book_callback

from loader import dp

@dp.message_handler(text_contains="Books")
async def select_category(message: Message):
    await message.answer(f"Choose courses:", reply_markup=categoryMenu)


@dp.callback_query_handler(text="level")
async def level_choose(call: CallbackQuery):
    await call.message.answer("Choose level", reply_markup=levelsMenu)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="books")
async def books_type(call: CallbackQuery):
    await call.message.answer("Books: ", reply_markup=booksMenu)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(book_callback.filter(item_name="nihongo_book"))
async def book_store(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.answer("Siz Nihongo_book tanladingiz",cache_time=60, show_alert=True)

@dp.callback_query_handler(text="back")
async def back_home(call: CallbackQuery):
    #replying and showing on the screen
    await call.message.edit_reply_markup(reply_markup=categoryMenu)
    await call.answer()