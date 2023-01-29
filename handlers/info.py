from aiogram import types


async def info(message: types.Message):
    await message.answer(text=f'Ваш id-{message.from_user.id}, ваш nickname-{message.from_user.first_name}, ваш '
                              f'username-{message.from_user.username}')
