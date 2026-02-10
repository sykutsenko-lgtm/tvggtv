from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import buttons

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [buttons.start_button, buttons.help_button],
        [buttons.quiz_button]
    ],
    resize_keyboard=True
)

quiz_topics_keyboard = InlineKeyboardMarkup([
    [buttons.science_button, buttons.history_button],
    [buttons.movies_button, buttons.geography_button],
    [buttons.sports_button]
])

new_quiz_keyboard = InlineKeyboardMarkup([
    [buttons.new_quiz_button]
])


def create_question_keyboard(options, question_index):
    keyboard_buttons = []
    for i, option in enumerate(options):
        keyboard_buttons.append([InlineKeyboardButton(
            option,
            callback_data=f"answer_{question_index}_{i}"
        )])
    return InlineKeyboardMarkup(keyboard_buttons)


def create_result_keyboard(options, selected_answer, correct_answer):
    keyboard_buttons = []
    for option in options:
        if option == correct_answer:
            keyboard_buttons.append([InlineKeyboardButton(f"✅ {option}", callback_data="no_action")])
        elif option == selected_answer and selected_answer != correct_answer:
            keyboard_buttons.append([InlineKeyboardButton(f"❌ {option}", callback_data="no_action")])
        else:
            keyboard_buttons.append([InlineKeyboardButton(option, callback_data="no_action")])

    keyboard_buttons.append([buttons.next_button])
    return InlineKeyboardMarkup(keyboard_buttons)