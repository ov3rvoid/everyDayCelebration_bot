from Config import dp, bot
from aiogram import types
from aiogram.dispatcher.filters import Command
from random import randint
from datetime import datetime 
from Parser import parsing

newdate = datetime.now()  
newdate = newdate.strftime("%d.%m.%Y")

smiles = ['🥳', '🥹', '😉', '💩', '🧐', '😎', '😶‍🌫️', '👻', '🤡', '🤯', '🎉', '🕊️']
len_smiles = len(smiles) - 1


def random_index(len_smiles):
    index = randint(0, len_smiles)
    return index


@dp.message_handler(commands= ['start'])
async def start(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        "Меня создали два гения"
    )

@dp.message_handler(commands='celebrate')
async def celebrate(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        f"{smiles[random_index(len_smiles)]}инициализирую поиск праздника\n\n{smiles[random_index(len_smiles)]}ща дропну",
    )