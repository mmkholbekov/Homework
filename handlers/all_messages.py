from aiogram import types


async def echo(message: types.Message):
    """
        Функция ответа заглавными буквами
    """
    await message.reply(text=message.text.upper())
