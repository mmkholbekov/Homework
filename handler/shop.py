from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

shop_kb = ReplyKeyboardMarkup(resize_keyboard=True)
shop_kb.add(
    KeyboardButton("Хочу iPhone X"),
    KeyboardButton("Хочу iPhone 11"),
    KeyboardButton("Хочу iPhone 12")
)
async def shop_start(cb: types.CallbackQuery):
    """
        Ответ на нажатие кнопки магазина
    """
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text="Выберите категорию из меню ниже",
        reply_markup=shop_kb
    )
