from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
from dotenv import load_dotenv
from os import getenv
import logging
from handler.start import start_command
from handler.help import help_command
from handler.pictures import image_sender
from handler.shop import shop_start
from handler.all_message import echo
from handler.shop_categories import show_phones



if __name__ == "__main__":
    # Наш бот
    load_dotenv()  # берем переменные окруженя из .env
    bot = Bot(getenv('BOT_TOKEN'))
    # Диспетчер, получает сообщения, обрабатывает через обработчик
    dp = Dispatcher(bot)

    # Регистрируем обработчики
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(image_sender, commands=['picture'])
    dp.register_callback_query_handler(shop_start, text='shop_start')
    dp.register_message_handler(show_phones, Text(equals='Хочу смартфон'))

    # Всегда в конце
    dp.register_message_handler(echo)
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
