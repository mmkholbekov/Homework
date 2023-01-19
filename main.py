from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
import logging

TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def echo(message: types.Message):
    await message.answer(text=f'Салам алейкум {message.from_user.first_name},я бот группы Python 25-3')



@dp.message_handler(commands="help")
async def echo(message: types.Message):
    await message.answer(text=f'Список команд: /start-Начало беседы с ботом, /help-Список команд с коротким описанием, /myinfo-Получить информацию о себе, /picture-Показать случайную картинку')
    await message.delete()


@dp.message_handler(commands="myinfo")
async def echo(message: types.Message):
    await message.answer(text=f'Ваш id-{message.from_user.id}, ваш nickname-{message.from_user.first_name}, ваш username-{message.from_user.username}')
    await message.delete()


@dp.message_handler(commands="picture")
async def echo(message: types.Message):
    await message.answer_photo(
        open('./media/dog.png', 'rb'),
        caption="Профессор Спайк"
    )
    await message.delete()



@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text.upper())

@dp.message_handler()
async def echo(message: types.Message):
    print(message)
    await message.answer(message.from_user.id, message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)