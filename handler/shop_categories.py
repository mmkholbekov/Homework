from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buy_item_kb = InlineKeyboardMarkup()
buy_item_kb.add(
    InlineKeyboardButton('Купить', callback_data='buy_ite')
)

async def show_phones(message: types.Message):
    """
        Функция показывает список смартфонов
    """
    await message.answer(text="Посмотри этот смартфон ")
    await message.answer_photo(open('./images/phon.jpg', 'rb'), caption="iPhone 5", reply_markup=buy_item_kb)


async def show_iphone(messange: types.Message):
    await messange.answer(text="iPhone 12", reply_markup=buy_item_kb)
    await messange.answer_photo(
        open('./images/phone3.jpg', 'rb')
    )

async def show_phones2(messange: types.Message):
    await messange.answer(text="iPhone 11", reply_markup=buy_item_kb)
    await messange.answer_photo(
        open('./images/phone.jpg', 'rb')
    )


