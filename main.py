import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import keyboards as kb
import requests

# Файл config с ключами необходимо создавать дополнительно
from config import TOKEN, API_KEY_SPORT

# Создаем объекты классов Bot (отвечает за взаимодействие с Telegram bot API) и Dispatcher (управляет обработкой входящих сообщений и команд)
bot = Bot(token=TOKEN)
dp = Dispatcher()


# Создаем класс Form, наследуемый от StatesGroup. Здесь будет храниться год
class Form(StatesGroup):
    year = State()

# Обработка команды /start
@dp.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    await message.answer("Привет! Здесь ты можешь узнать состав любимой команды НБА с 2021 по 2023 год\n"
        "Введи интересующий год:")
    await state.set_state(Form.year)

# Сохраняем год и создаем меню выбора конференции
@dp.message(Form.year)
async def name(message: Message, state: FSMContext):
    await state.update_data(year=message.text)
    await message.answer(
        "Выбери конференцию:", reply_markup=await kb.conf_keyboard())

# Обработка кнопки East Выводим список-кнопок для восточной конференции
@dp.callback_query(F.data == 'east')
async def east_conf(callback: CallbackQuery):
    await callback.message.answer('Выбери команду:', reply_markup=await kb.east_keyboard())

# Обработка кнопки West  Выводим список-кнопок для западной конференции
@dp.callback_query(F.data == 'west')
async def west_conf(callback: CallbackQuery):
    await callback.message.answer('Выбери команду:', reply_markup=await kb.west_keyboard())

# Ловим колбэки, начинающиеся с "team_"
@dp.callback_query(F.data.startswith("team_"))
async def team(callback: CallbackQuery, state: FSMContext):
    # Достаем год из контекста состояния
    user_data = await state.get_data()
    year = user_data['year']
    # Извлекаем ID команды Разделяем строку и берем второй элемент
    team_id = callback.data.split("_")[1]
    # Формируем url и headers
    url = f"https://v2.nba.api-sports.io/players?team={team_id}&season={year}"  # Подставляем team_id и year
    headers = {
        'x-rapidapi-key': API_KEY_SPORT,
        'x-rapidapi-host': 'v2.nba.api-sports.io'
    }
    # Делаем запрос к API
    response = requests.get(url, headers=headers)
    # Если запрос удачный
    if response.status_code == 200:
        # Преобразуем в json
        data = response.json()
        # Достаем список игроков
        players = data.get('response', [])
        # Формируем сообщение с игроками
        message_text = f"Состав команды в {year} году:\n"
        for player in players:
            message_text += f"- {player['firstname']} {player['lastname']}\n"
        # Выводим список игроков
        await callback.message.answer(message_text)
    else:
        await callback.message.answer("Ошибка при запросе к API 😕")
    # Закрываем уведомление
    await callback.answer()

# Создаем асинхронную функцию main, которая будет запускать наш бот
async def main():
    await dp.start_polling(bot)

# Запускаем асинхронную функцию main
if __name__ == '__main__':
    asyncio.run(main())