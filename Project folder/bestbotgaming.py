import logging
import random
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6776361555:AAHeFLJrzRefrGv4YvFmZgVv5gDfc10xFtI'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Вам неоюходимо отправить\n/start_bot")
    print(f"-------------------------\nnick name: {message.from_user.first_name}\nuser name: {message.from_user.username}\n------------------------------------------\n")


@dp.message_handler(commands=['start_bot'])
async def start_bot(message: types.Message):
    await message.answer(f"{message.from_user.first_name} Добро Пожаловать на Best Bot Gaming!\nВ этом боте много интересных игр. @zufar_BRO Создатель бота. /game_list для списков игр")

@dp.message_handler(commands=['game_list'])
async def GameList(message: types.Message):
    await message.answer(f"{message.from_user.first_name}Вот вам Список игр\n/GUESS - Угадай Число\n/QUIZ - Математическое викторина")


@dp.message_handler(commands=['guess'])
async def guess_number(message: types.Message):
    await message.answer("Давай сыграем в 'Угадай число'! Я загадаю число от 1 до 10, а ты попробуй угадать.")
    number_to_guess = random.randint(1, 10)

    @dp.message_handler()
    async def check_guess(msg: types.Message):
        try:
            user_number = int(msg.text)
        except ValueError:
            return await msg.answer("Пожалуйста, введите число.")

        if user_number < number_to_guess:
            await msg.answer("Загаданное число больше.")
        elif user_number > number_to_guess:
            await msg.answer("Загаданное число меньше.")
        else:

            await msg.answer(f"Поздравляю, ты угадал число!")
            dp.message_handlers.unregister(check_guess)  # Удаляем обработчик после угадывания числа


@dp.message_handler(commands=['quiz'])
async def math_quiz(message: types.Message):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_answer = num1 + num2
    question_text = f"Сколько будет {num1} + {num2}?"

    await message.answer(f"Давай сыграем в 'Математическую Викторину'! {question_text}")

    @dp.message_handler()
    async def check_answer(msg: types.Message):
        try:
            user_answer = int(msg.text)
        except ValueError:
            return await msg.answer("Пожалуйста, введите число.")

        if user_answer == correct_answer:

            await msg.answer(f"Поздравляю, ты решил пример правильно!")
        else:
            await msg.answer("Ты ошибся. Попробуй еще раз /quiz.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
