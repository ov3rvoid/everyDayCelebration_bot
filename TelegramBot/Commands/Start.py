from Config import dp, bot
from aiogram import types
from aiogram.dispatcher.filters import Command


@dp.message_handler(commands= ['start'])
async def start(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        "Меня создали два гения"
    )