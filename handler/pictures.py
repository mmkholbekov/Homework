from aiogram import types


async def image_sender(message: types.Message):
    """
        Функция ответа пользователю картинкой
    """
    await message.answer_photo(
        open('./images/phone.jpg', 'rb'),
        caption="Phone"
    )
    await message.delete()