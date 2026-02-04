from pyrogram.types import KeyboardButton, InlineKeyboardButton

start_button = KeyboardButton("Старт")
help_button = KeyboardButton("Помощь")
quiz_button = KeyboardButton("Викторина")

science_button = InlineKeyboardButton("Наука", callback_data="quiz_science")
history_button = InlineKeyboardButton("История", callback_data="quiz_history")
movies_button = InlineKeyboardButton("Фильмы", callback_data="quiz_movies")
next_button = InlineKeyboardButton("Далее ▶️", callback_data="next_question")
new_quiz_button = InlineKeyboardButton("Новая викторина", callback_data="new_quiz")