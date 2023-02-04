from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from os import getenv
import logging

from handlers import info
from handlers.constants import HELP_TEXT, START_TEXT
from handlers.start import start_command
from handlers.help import help_command
# from handlers.info import info
from handlers.pictures import image_sender
from handlers.shop import shop_start, adress
from handlers.all_messages import echo
from handlers.shop_categories import show_product, show_phone
from handlers.admin import example
from handlers.admin import (
    example,
    check_curses,
    ban_user
)

from handlers.user_info_form import (
    Form,
    cancel_handler,
    form_start,
    process_name,
    process_age,
    process_day,
    process_done
)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # Наш бот
    load_dotenv()  # берем переменные окруженя из .env
    bot = Bot(getenv('BOT_TOKEN'))
    # Диспетчер, получает сообщения, обрабатывает через обработчик
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    # Регистрируем обработчики
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(image_sender, commands=['picture'])
    dp.register_message_handler(form_start, commands=['form'])
    dp.register_message_handler(form_start, Text(equals='Нет'), state=Form.done)
    dp.register_message_handler(info, commands=['myinfo'])
    dp.register_callback_query_handler(shop_start, text='shop_start')
    dp.register_callback_query_handler(adress, text='adress')
    dp.register_message_handler(show_product, commands=['phone'])
    dp.register_message_handler(show_phone, Text(equals='Показать смартфон'))
    dp.register_message_handler(ban_user, commands=['да'], commands_prefix='!/')
    dp.register_message_handler(cancel_handler, state='*', commands='cancel')
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(process_name, state=Form.name)
    dp.register_message_handler(process_age, state=Form.age)
    dp.register_message_handler(process_day, state=Form.day)
    dp.register_message_handler(process_done, Text(equals='Да'), state=Form.done)
    # Всегда в конце
    dp.register_message_handler(check_curses)

    executor.start_polling(dp, skip_updates=True)

    dp.register_message_handler(example)
    dp.register_message_handler(echo)
