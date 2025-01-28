import telegram as telegram
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callbackData import course_callback, book_callback

categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📊 Levels", callback_data='level'),
        ],
        [
            InlineKeyboardButton(text="🔹Courses", callback_data='course'),
            InlineKeyboardButton(text="📚 Books", callback_data='books'),
        ],

        [
            InlineKeyboardButton(text="Tests", callback_data='tests'),
            InlineKeyboardButton(text="Quizzes", callback_data='quizzes'),
        ],
        [
            InlineKeyboardButton(text="🔎Search", switch_inline_query_current_chat=""),
        ],

    ],

)


#Keyboard for courses:
levelsMenu = InlineKeyboardMarkup(row_width=1)

n5 = InlineKeyboardButton(text="Level N5", callback_data=course_callback.new(item_name="n5"))
levelsMenu.insert(n5)
n4 = InlineKeyboardButton(text="Level N4", callback_data=course_callback.new(item_name="n4"))
levelsMenu.insert(n4)
n3 = InlineKeyboardButton(text="Level N3", callback_data=course_callback.new(item_name="n3"))
levelsMenu.insert(n3)
n2 = InlineKeyboardButton(text="Level N2", callback_data=course_callback.new(item_name="n2"))
levelsMenu.insert(n2)
back_button = InlineKeyboardButton(text="🔙Back", callback_data="back")
levelsMenu.insert(back_button)

#3-usul

books = {
    "Minono Nihongo": "nihongo_book",
    "Words": "new_words",
    "Kanji": "kanji_book",
    "Rekishi": "story_book",
}

booksMenu = InlineKeyboardMarkup(row_width=1)
for key, value in books.items():
    booksMenu.insert(InlineKeyboardButton(text=key, callback_data=book_callback.new(item_name=value)))
booksMenu.insert(back_button)

#button for each course
telegram_keyboard = InlineKeyboardMarkup(inlines=telegram)

