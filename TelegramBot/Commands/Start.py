from aiogram import types
from aiogram.dispatcher.filters import Command

from random import randint
from datetime import datetime

from Parser import output_celebrates
from Config import dp, bot
from Keyboards import *


newdate = datetime.now()
newdate = newdate.strftime("%d.%m.%Y")

day_week = datetime.weekday(datetime.now())
week = datetime.isocalendar(datetime.now()).week

def check_week(days_list, day_week, week):
    if week % 2 != 0:
        return f"Сегодня {days_list[day_week]}, верхняя неделя"
    elif week % 2 == 0:
        return f"Сегодня {days_list[day_week]}, нижняя неделя"
    else:
        return f"кажется чето отъебнуло, не ебу какая неделя"

smiles = ['🥳', '🥹', '😉', '💩', '🧐', '😎', '😶‍🌫️', '👻', '🤡', '🤯', '🎉', '🕊️']
len_smiles = len(smiles) - 1


def random_celebrity():
    index = randint(0, len(output_celebrates))
    return index

def random_index(len_smiles):
    index = randint(0, len_smiles)
    return index


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(
        "Меня создали два гения"
    )


@dp.message_handler(commands='celebrate')
async def celebrate(message: types.Message):
    await message.reply(
        f"{smiles[random_index(len_smiles)]}Каждый день праздник)))",
    )
    await message.reply(
        output_celebrates[random_celebrity()]
    )
    


@dp.message_handler(commands='shedule')
async def shedule(message: types.Message):
    await message.reply(
        "Чё там по парам",
        reply_markup=days_kb
    )

# --------------------------------------------------------------------------


# Верхняя неделя
@dp.callback_query_handler(lambda c: c.data == 'mon1')
async def mon1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(
        f'Понедельник, верхняя неделя\n\n3 пара (12:40 — 14:15)\nПрограммирование и алгоритмизация (Лекционные)\nПолевой Д. В.\nБ-4\n\n4 пара (14:30 — 16:05)\nВведение в специальность (Лекционные)\nБакулев К. С.\nБ-734\n\n{check_week(days_list, day_week, week)}',
        reply_markup=days_kb
    )


@dp.callback_query_handler(lambda c: c.data == 'tue1')
async def tue1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(
        f'Вторник, верхняя неделя\n\n2 пара (10:50 — 12:25)\nАнгем (Лекционные)\nПлужникова Е. Л.\nБ-3\n\n4 пара (14:30 — 16:05)\nИностранный язык (Практические)\nКаф. ИЯКТ\n\n5 пара (16:20 — 17:55)\nАнгем (Практические)\nДанченков И. В.\nА-328\n\n{check_week(days_list, day_week, week)}',
        reply_markup=days_kb
    )


@dp.callback_query_handler(lambda c: c.data == 'wed1')
async def wed1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(
        f'Среда, верхняя неделя\n\n4 пара (14:30 — 16:05)\nИстория России (Практические)\nАристов А. В.\nА-509\n\n5 пара (16:20 — 17:55)\nИстория России (Лекционные)\nНауменко О. А.\nБ-3\n\n{check_week(days_list, day_week, week)}',
        reply_markup=days_kb
    )


@dp.callback_query_handler(lambda c: c.data == 'thu1')
async def thu1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(
        f'Четверг, верхняя неделя\n\n1 пара (09:00 — 10:35)\nИстория России (Лекционные)\nНауменко О. А.\nБ-734\n\n2 пара (10:50 — 12:25)\nМатематика (Лекционные)\nПлужникова Е. Л.\nБ-3\n\n3 пара (12:40 — 14:15)\nОсновы российской государственности (Практические)\nВакансия 3 К. .\nА-517\n\n4 пара (14:30 — 16:05)\nИностранный язык (Практические)\nКаф. ИЯКТ\n\n{check_week(days_list, day_week, week)}',
        reply_markup=days_kb
    )


@dp.callback_query_handler(lambda c: c.data == 'fri1')
async def fri1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(
        f'Пятница, верхняя неделя\n\n2 пара (10:50 — 12:25)\nВычислительные машины, сети и системы (Лекционные)\nКрынецкая Г. С.\nБ-3\n\n3 пара (12:40 — 14:15)\nОсновы российской государственности (Лекционные)\nВакансия 3 К. .\nА-308\n\n4 пара (14:30 — 16:05)\nМатематика (Практические)\nПлужникова Е. Л.\nЛ-631\n\n5 пара (16:20 — 17:55)\nМатематика (Практические)\nПлужникова Е. Л.\nЛ-631\n\n{check_week(days_list, day_week, week)}',
        reply_markup=days_kb
    )

# Нижняя неделя
@dp.callback_query_handler(lambda c: c.data == 'mon2')
async def mon2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(
        f'Понедельник, нижняя неделя\n\n2 пара (10:50 — 12:25)\n1 п.г. Вычислительные машины, сети и системы (Лабораторные)\nКрынецкая Г. С.\nБ-901\n\n3 пара (12:40 — 14:15)\nПрограммирование и алгоритмизация (Лекционные)\nПолевой Д. В.\nБ-4\n\n4 пара (14:30 — 16:05)\nВведение в специальность (Лекционные)\nБакулев К. С.\nБ-734\n\n{check_week(days_list, day_week, week)}',
        reply_markup=days_kb
    )


@dp.callback_query_handler(lambda c: c.data == 'tue2')
async def tue2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(
        f'Вторник, нижняя неделя\n\n2 пара (10:50 — 12:25)\nМатематика (Лекционные)\nПлужникова Е. Л.\nБ-3\n\n4 пара (14:30 — 16:05)\nИностранный язык (Практические)\nКаф. ИЯКТ\n\n{check_week(days_list, day_week, week)}',
        reply_markup=days_kb
    )


@dp.callback_query_handler(lambda c: c.data == 'wed2')
async def wed2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(
        f'Среда, нижняя неделя\n\n3 пара (12:40 — 14:15)\nВведение в специальность (Практические)\nЕфимов Д. А.\nГ-562\n\n4 пара (14:30 — 16:05)\nАнгем (Практические)\nДанченков И. В.\nА-321\n\n5 пара (16:20 — 17:55)\\nИстория России (Лекционные)\nНауменко О. А.\nБ-3\n\n{check_week(days_list, day_week, week)}',
        reply_markup=days_kb
    )


@dp.callback_query_handler(lambda c: c.data == 'thu2')
async def thu2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(
        f'Четверг, нижняя неделя\n\n2 пара (10:50 — 12:25)\nМатематика (Лекционные)\nПлужникова Е. Л.\nБ-3\n\n3 пара (12:40 — 14:15)\nОсновы российской государственности (Практические)\nВакансия 3 К. .\nА-517\n\n4 пара (14:30 — 16:05)\nИностранный язык (Практические)\nКаф. ИЯКТ\n\n{check_week(days_list, day_week, week)}',
        reply_markup=days_kb
    )


@dp.callback_query_handler(lambda c: c.data == 'fri2')
async def fri2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(
        f'Пятница, нижняя неделя\n\n1 пара (09:00 — 10:35)\nПрограммирование и алгоритмизация (Практические)\nПолевой Д. В.\nБ-829\n\n2 пара (10:50 — 12:25)\nМатематика (Практические)\nПлужникова Е. Л.\nА-512\n\n3 пара (12:40 — 14:15)\nМатематика (Практические)\nПлужникова Е. Л.\nА-512\n\n4 пара (14:30 — 16:05)\nВычислительные машины, сети и системы (Лекционные)\nКрынецкая Г. С.\nБ-3\n\n{check_week(days_list, day_week, week)}',
        reply_markup=days_kb
    )
