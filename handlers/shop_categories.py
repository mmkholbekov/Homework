from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


buy_item_kb = InlineKeyboardMarkup()
buy_item_kb.add(
    InlineKeyboardButton('Купить', callback_data='buy_item')
)


async def show_product(message: types.Message):
    """
        Функция показывает список товаров
    """

    await message.answer(text="Взглянь на этот товар")
    await message.answer_photo(
        open('./images/dog.png', 'rb'), caption="Air pods 2", reply_markup=buy_item_kb)


async def show_phone(messange: types.Message):
    await messange.answer(text="Зарядка", reply_markup=buy_item_kb)
    await messange.answer_photo(
        open('./images/phone3.jpg', 'rb')
    )


async def show_phones2(messange: types.Message):
    await messange.answer(text="iPhone 11", reply_markup=buy_item_kb)
    await messange.answer_photo(
        open('./images/phone.jpg', 'rb')
    )
