from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

days_list = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'восскресенье']
days_list1 = [['Пн', 'mon1'], ['Вт', 'tue1'], ['Ср', 'wed1'], ['Чт', 'thu1'], ['Пт', 'fri1']]
days_list2 = [['Пн', 'mon2'], ['Вт', 'tue2'], ['Ср', 'wed2'], ['Чт', 'thu2'], ['Пт', 'fri2']]


days_kb = InlineKeyboardMarkup(row_width=5)

for day in range(len(days_list1)):
    days_kb.insert(InlineKeyboardButton(text=days_list1[day][0], callback_data=days_list1[day][1]))

for day in range(len(days_list2)):
    days_kb.insert(InlineKeyboardButton(text=days_list2[day][0], callback_data=days_list2[day][1]))
