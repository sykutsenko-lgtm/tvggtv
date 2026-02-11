from pyrogram import Client, filters
from pyrogram.types import Message
import config
import buttons
import keyboards
from custom_filters import button_filter
import random

bot = Client(
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    name="qwez_bot",
)

quiz_questions = {
    "science": [
        {
            "question": "Сколько планет в Солнечной системе?",
            "options": ["7", "8", "9", "10"],
            "answer": "8"
        },
        {
            "question": "Какой газ преобладает в атмосфере Земли?",
            "options": ["Кислород", "Азот", "Углекислый газ", "Водород"],
            "answer": "Азот"
        },
        {
            "question": "Какая самая близкая к Земле звезда?",
            "options": ["Сириус", "Полярная", "Солнце", "Альфа Центавра"],
            "answer": "Солнце"
        },
        {
            "question": "Как называется процесс фотосинтеза у растений?",
            "options": ["Дыхание", "Питание", "Синтез света", "Преобразование энергии"],
            "answer": "Синтез света"
        },
        {
            "question": "Какой химический элемент обозначается символом Au?",
            "options": ["Серебро", "Золото", "Алюминий", "Аргон"],
            "answer": "Золото"
        },
    ],
    "history": [
        {
            "question": "В каком году началась Вторая мировая война?",
            "options": ["1938", "1939", "1940", "1941"],
            "answer": "1939"
        },
        {
            "question": "Кто был первым президентом США?",
            "options": ["Джефферсон", "Линкольн", "Вашингтон", "Рузвельт"],
            "answer": "Вашингтон"
        },
        {
            "question": "В каком году человек впервые полетел в космос?",
            "options": ["1957", "1961", "1969", "1975"],
            "answer": "1961"
        },
        {
            "question": "Кто написал 'Войну и мир'?",
            "options": ["Достоевский", "Толстой", "Чехов", "Пушкин"],
            "answer": "Толстой"
        },
        {
            "question": "Какой город был столицей Византийской империи?",
            "options": ["Рим", "Афины", "Константинополь", "Александрия"],
            "answer": "Константинополь"
        },
    ],
    "movies": [
        {
            "question": "Кто режиссер фильма 'Крестный отец'?",
            "options": ["Скорсезе", "Коппола", "Тарантино", "Нолан"],
            "answer": "Коппола"
        },
        {
            "question": "Сколько частей в 'Гарри Поттере'?",
            "options": ["6", "7", "8", "9"],
            "answer": "8"
        },
        {
            "question": "Кто сыграл главную роль в 'Титанике'?",
            "options": ["Брэд Питт", "Леонардо ДиКаприо", "Джонни Депп", "Том Круз"],
            "answer": "Леонардо ДиКаприо"
        },
        {
            "question": "Какой фильм получил больше всего Оскаров?",
            "options": ["Титаник", "Властелин колец", "Бен-Гур", "Все эти"],
            "answer": "Все эти"
        },
        {
            "question": "Кто режиссер 'Парка Юрского периода'?",
            "options": ["Стивен Спилберг", "Джеймс Кэмерон", "Джордж Лукас", "Кристофер Нолан"],
            "answer": "Стивен Спилберг"
        },
    ],
    "geography": [
        {
            "question": "Какая самая длинная река в мире?",
            "options": ["Амазонка", "Нил", "Янцзы", "Миссисипи"],
            "answer": "Нил"
        },
        {
            "question": "В какой стране находится Эйфелева башня?",
            "options": ["Италия", "Франция", "Испания", "Германия"],
            "answer": "Франция"
        },
        {
            "question": "Какой океан самый большой?",
            "options": ["Атлантический", "Индийский", "Тихий", "Северный Ледовитый"],
            "answer": "Тихий"
        },
        {
            "question": "Столица Японии?",
            "options": ["Пекин", "Сеул", "Токио", "Бангкок"],
            "answer": "Токио"
        },
        {
            "question": "Какая пустыня самая большая в мире?",
            "options": ["Сахара", "Гоби", "Аравийская", "Антарктическая"],
            "answer": "Антарктическая"
        },
    ],
    "sports": [
        {
            "question": "Сколько игроков в футбольной команде на поле?",
            "options": ["10", "11", "12", "9"],
            "answer": "11"
        },
        {
            "question": "В каком виде спорта используется ракетка?",
            "options": ["Футбол", "Теннис", "Баскетбол", "Волейбол"],
            "answer": "Теннис"
        },
        {
            "question": "Сколько периодов в хоккейном матче?",
            "options": ["2", "3", "4", "5"],
            "answer": "3"
        },
        {
            "question": "Какой вид спорта называется 'королевой спорта'?",
            "options": ["Футбол", "Легкая атлетика", "Плавание", "Гимнастика"],
            "answer": "Легкая атлетика"
        },
        {
            "question": "Сколько очков дается за трехочковый бросок в баскетболе?",
            "options": ["2", "3", "4", "1"],
            "answer": "3"
        },
    ]
}

user_data = {}


@bot.on_message(filters.command("start") | button_filter(buttons.start_button))
async def start_handler(client: Client, message: Message):
    await message.reply(
        "Привет! Это бот викторина. Чтобы начать напиши /quiz, а если что то непонятно нажми /help",
        reply_markup=keyboards.main_keyboard
    )


@bot.on_message(filters.command("help") | button_filter(buttons.help_button))
async def help_handler(client: Client, message: Message):
    await message.reply(
        "Это помощь \nКоманды: \n/start \n/help \n/quiz",
        reply_markup=keyboards.main_keyboard
    )


@bot.on_message(filters.command("quiz") | button_filter(buttons.quiz_button))
async def quiz_start(client: Client, message: Message):
    await message.reply("Выберите тему викторины:", reply_markup=keyboards.quiz_topics_keyboard)


@bot.on_callback_query(filters.regex(r"^quiz_"))
async def quiz_topic_selection(client, callback_query):
    topic = callback_query.data.split("_")[1]
    user_id = callback_query.from_user.id

    questions = quiz_questions[topic].copy()
    random.shuffle(questions)
    questions = questions[:5]

    user_data[user_id] = {
        "topic": topic,
        "questions": questions,
        "current": 0,
        "score": 0,
        "state": "in_quiz"
    }

    await send_question(client, callback_query, user_id)
    await callback_query.answer()


async def send_question(client, callback_query, user_id):
    data = user_data[user_id]

    if data["current"] >= len(data["questions"]):
        await finish_quiz(client, callback_query, user_id)
        return

    question_data = data["questions"][data["current"]]
    text = f"Вопрос {data['current'] + 1}/{len(data['questions'])}\n{question_data['question']}"

    keyboard = keyboards.create_question_keyboard(question_data["options"], data["current"])

    if callback_query.message.reply_markup:
        await callback_query.message.edit_text(text, reply_markup=keyboard)
    else:
        await callback_query.message.reply(text, reply_markup=keyboard)


@bot.on_callback_query(filters.regex(r"^answer_"))
async def answer_handler(client, callback_query):
    user_id = callback_query.from_user.id

    if user_id not in user_data or user_data[user_id]["state"] != "in_quiz":
        await callback_query.answer("Викторина завершена или не начата")
        return

    data = user_data[user_id]
    question_index = int(callback_query.data.split("_")[1])
    answer_index = int(callback_query.data.split("_")[2])

    if question_index != data["current"]:
        await callback_query.answer("Этот вопрос уже пройден")
        return

    current_question = data["questions"][question_index]
    selected_answer = current_question["options"][answer_index]
    correct_answer = current_question["answer"]

    if selected_answer == correct_answer:
        data["score"] += 1
        result_text = "✅ Правильно!"
    else:
        result_text = f"❌ Неправильно! Правильный ответ: {correct_answer}"

    keyboard = keyboards.create_result_keyboard(current_question["options"], selected_answer, correct_answer)
    text = f"Вопрос {data['current'] + 1}/{len(data['questions'])}\n{current_question['question']}\n\n{result_text}"

    await callback_query.message.edit_text(text, reply_markup=keyboard)
    await callback_query.answer()


@bot.on_callback_query(filters.regex(r"^next_question$"))
async def next_question_handler(client, callback_query):
    user_id = callback_query.from_user.id

    if user_id not in user_data:
        await callback_query.answer("Викторина завершена")
        return

    data = user_data[user_id]
    data["current"] += 1

    if data["current"] >= len(data["questions"]):
        await finish_quiz(client, callback_query, user_id)
    else:
        await send_question(client, callback_query, user_id)

    await callback_query.answer()


async def finish_quiz(client, callback_query, user_id):
    data = user_data[user_id]
    score = data["score"]
    total = len(data["questions"])

    percentage = (score / total) * 100

    result_text = f"🎉 Викторина завершена!\nТема: {data['topic']}\nРезультат: {score}/{total} ({percentage:.0f}%)\n"

    if score == total:
        result_text += "🏆 Отлично! Все ответы верны!"
    elif score >= total * 0.8:
        result_text += "👍 Отличный результат!"
    elif score >= total * 0.6:
        result_text += "👌 Хороший результат!"
    elif score >= total * 0.4:
        result_text += "😐 Неплохо, но можно лучше!"
    else:
        result_text += "💪 Попробуйте еще раз!"

    await callback_query.message.edit_text(result_text, reply_markup=keyboards.new_quiz_keyboard)
    del user_data[user_id]


@bot.on_callback_query(filters.regex(r"^new_quiz$"))
async def new_quiz_handler(client, callback_query):
    await callback_query.message.edit_text("Выберите тему викторины:", reply_markup=keyboards.quiz_topics_keyboard)
    await callback_query.answer()


if __name__ == "__main__":
    print("Бот запускается...")
    bot.run()