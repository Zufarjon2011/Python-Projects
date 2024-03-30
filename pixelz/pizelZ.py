import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from time import sleep

API_TOKEN = '6772864581:AAGJsK0haLQmbtcyyGXFFw3576X0eXmTbyk'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN,  disable_web_page_preview=True)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


async def check_subscription(user_id):
    status = ['creator', 'administrator', 'member']
    for i in status:
        chat_member = await bot.get_chat_member(chat_id="-1002084284400", user_id=user_id)
        if chat_member.status == i:
            return i  # Return the status if subscribed
    return None  # Return None if not subscribed

async def welcome_user(message):
    await message.reply(f"{message.from_user.first_name} Вы подписались на наш канал"
                        f"Теперь вы можете использовать наш бот\n"
                        f"Вам необходимо отправить\n"
                        f"/start_bot")

async def prompt_subscription(message):
    await message.reply("Для использования бота, пожалуйста подпишитесь на [канал](https://t.me/pixelZ_z).", parse_mode=types.ParseMode.MARKDOWN)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    print(f"-------------------------\n"
          f"nick name: {message.from_user.first_name}\n"
          f"user name: {message.from_user.username}\n"
          f"-------------------------\n")

    user_id = message.from_user.id
    subscription_status = await check_subscription(user_id)
    if subscription_status:
        await welcome_user(message)
    else:
        await prompt_subscription(message)


@dp.message_handler(commands=['start_bot'])
async def start(message: types.Message):
    await message.answer(f"{message.from_user.first_name}!\n"
                         f"Этот бот будет отправлять вам Фото на качественных пикселях\n"
                         f"На котором Будет Выглядеть Круче!\n"
                         f"/List для Лист пикселей\n"
                         f"\n"
                         f"Создатель Бота @zufar_BRO")


@dp.message_handler(commands=['list'])
async def start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Машины", callback_data="car"))
    keyboard.add(types.InlineKeyboardButton(text="Прогромирования", callback_data="prg"))
    keyboard.add(types.InlineKeyboardButton(text="Другие", callback_data="other"))

    await bot.send_message(message.chat.id, f"{message.from_user.first_name} Лист пикселей\n"
                                            f"Быберите пикслей с кнопок", reply_markup=keyboard)



@dp.callback_query_handler(lambda query: query.data == 'car')
async def process_callback_button_pressed(callback_query: types.CallbackQuery):
    with open('Supra.jpg', 'rb') as photo:
        await bot.send_photo(callback_query.from_user.id, photo, caption='Тойота Супра 1993\n'
                                                                         'Легендарная машина\n'
                                                                         '\n'
                                                                         'Отличная рисунок для Рабочего стола!')
    sleep(1)
    with open('Rangerover.jpg', 'rb') as photo:
        await bot.send_photo(callback_query.from_user.id, photo,  caption='Рендж Ровер Велар 2023\n'
                                                                  'Машина премиум класса\n'
                                                                  '\n'
                                                                  'Отличная рисунок для Рабочего стола!')

@dp.callback_query_handler(lambda query: query.data == 'prg')
async def process_callback_button_pressed(callback_query: types.CallbackQuery):
    with open('Programming.jpg', 'rb') as photo:
        await bot.send_photo(callback_query.from_user.id, photo, caption='Прогромирования\n'
                                                                         'Да, мы так и пишем код\n'
                                                                         '\n'
                                                                         'Отличная рисунок для Рабочего стола!')
    sleep(1)
    with open('Laptop.jpg', 'rb') as photo:
        await bot.send_photo(callback_query.from_user.id, photo , caption='Прогромирования на лаптопе\n'
                                                                  'тут уже по комфортнее\n'
                                                                  '\n'
                                                                  'Отличная рисунок для Рабочего стола!')
@dp.callback_query_handler(lambda query: query.data == 'other')
async def process_callback_button_pressed(callback_query: types.CallbackQuery):
    with open('spiderman.jpg', 'rb') as photo:
        await bot.send_photo(callback_query.from_user.id, photo, caption='Человек Паук\n'
                                                                         'Чкс Чкс это Человек Паук\n'
                                                                         '\n'
                                                                         'Отличная рисунок для Рабочего стола!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
