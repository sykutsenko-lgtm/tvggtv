from pyrogram import filters
from pyrogram.types import Message, CallbackQuery

def button_filter(button):
    async def func(_, __, message: Message):
        return message.text == button.text
    return filters.create(func, "ButtonFilter", button=button)

def inline_button_filter(callback_data):
    async def func(_, __, query: CallbackQuery):
        return query.data == callback_data
    return filters.create(func, "InlineButtonFilter", callback_data=callback_data)