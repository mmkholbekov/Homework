from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters import Text
from dotenv import load_dotenv
from os import getenv
import logging
from handlers.constants import HELP_TEXT, START_TEXT
from handlers.start import start_command
from handlers.help import help_command
from handlers.info import info
from handlers.pictures import image_sender
from handlers.shop import shop_start, adress
from handlers.all_messages import echo
from handlers.shop_categories import show_product, show_phone, show_phones2
from handlers.admin import example
from handlers.admin import (
    example,
    check_curses,
    ban_user
)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # Наш бот
    load_dotenv()  # берем переменные окруженя из .env
    bot = Bot(getenv('BOT_TOKEN'))
    # Диспетчер, получает сообщения, обрабатывает через обработчик
    dp = Dispatcher(bot)

    # Регистрируем обработчики
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(image_sender, commands=['picture'])
    dp.register_message_handler(info, commands=['myinfo'])
    dp.register_callback_query_handler(shop_start, text='shop_start')
    dp.register_callback_query_handler(adress, text='adress')
    dp.register_message_handler(show_product, commands=['phone'])
    dp.register_message_handler(show_phone, Text(equals='Показать смартфон'))
    dp.register_message_handler(ban_user, commands=['да'], commands_prefix='!/')

    # # Всегда в конце
    dp.register_message_handler(check_curses)

    executor.start_polling(dp, skip_updates=True)

    dp.register_message_handler(example)
    dp.register_message_handler(echo)


