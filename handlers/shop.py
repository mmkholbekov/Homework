from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

shop_kb = ReplyKeyboardMarkup(resize_keyboard=True)
shop_kb.add(
    KeyboardButton("Хочу смартфон"),
    KeyboardButton("Хочу нотбук"),
    KeyboardButton("Хочу наушники"),
)


async def shop_start(cb: types.CallbackQuery):
    """
        Ответ на нажатие кнопки магазина,
        Показываем категории кнопками
    """
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text="Выберите категорию из меню ниже",
        reply_markup=shop_kb
    )


async def adress(cb: types.CallbackQuery):
    """
        Ответ на нажатие кнопки Адрес
    """
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text="Наш адрес: город Бишкек ул Ибраимова 103Б",
        reply_markup=shop_kb
    )


