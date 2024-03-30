import logging
from aiogram import Bot, Dispatcher, executor, types
from time import sleep

API_TOKEN = '6772864581:AAGJsK0haLQmbtcyyGXFFw3576X0eXmTbyk'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Вам необходимо отправить\n/start_bot")
    print(f"-------------------------\nnick name: {message.from_user.first_name}\nuser name: {message.from_user.username}\n-------------------------\n")

@dp.message_handler(commands=['start_bot'])
async def start(message: types.Message):
    await message.answer(f"Здравствуйте {message.from_user.first_name}!\nЭтот бот будет отправлять вам Фото на Фикселях\nНа котором Будет Выглядеть Круче!\n/List для Лист пикселей\n\nСоздатель Бота @zufar_BRO")


@dp.message_handler(commands=['list'])
async def start(message: types.Message):
    await message.answer(f"{message.from_user.first_name} Вот вам Лист\n/CAR - Машины\n/PRG - Программирование\n/other - Другие")

@dp.message_handler(commands=['CAR'])
async def start(message: types.Message):
    with open('Supra.jpg', 'rb') as photo:
        await bot.send_photo(message.chat.id, photo, caption='Тойота Супра 1993')
    sleep(1)
    with open('Rangerover.jpg', 'rb') as photo:
        await bot.send_photo(message.chat.id, photo, caption='Рендж Ровер Велар 2023')
@dp.message_handler(commands=['PRG'])
async def start(message: types.Message):
    with open('Programming.jpg', 'rb') as photo:
        await bot.send_photo(message.chat.id, photo, caption='Прогромирования')
    sleep(1)
    with open('Laptop.jpg', 'rb') as photo:
        await bot.send_photo(message.chat.id, photo, caption='Прогромипрвания на Лаптопе')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
