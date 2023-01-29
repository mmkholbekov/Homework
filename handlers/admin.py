from aiogram import types
from handlers.constants import CURSES_TEXT


async def example(message: types.Message):
    """
        функция чтоб получать
        в логах сведения о сообщениях и тд
    """
    print(f"{message.chat.type=}")
    print(f"{message.reply_to_message=}")
    print(f"{message.from_user.id=}")
    if message.chat.type != 'private':
        admins = await message.chat.get_administrators()
        print(admins)


async def check_user_is_admin(message: types.Message):
    """
    Функция для проверки прав админа автора сообщения
    в том чате, в который сообщение было отправлено
    """
    admins = await message.chat.get_administrators()
    for admin in admins:
        if admin["user"]["id"] == message.from_user.id:
            return True
    return False


async def check_curses(message: types.Message):
    """
    проверка, содержит ли сообщение плохие слова
    """
    BAD_WORDS = ["дурак", "дурачок", "бля", "бляя"]
    if message.chat.type != 'private':
        for word in BAD_WORDS:
            if message.text.lower().replace(' ', '').count(word):
                await message.answer(
                    text=CURSES_TEXT.format(
                        first_name=message.from_user.first_name
                    ))

                await message.reply(f'Пользователь {message.from_user.first_name}: отправил плохое слово '
                                    f'Администраторы забанить {message.from_user.first_name}: Да/Нет?')
                break


async def ban_user(message: types.Message):
    """
    обработчик, чтоб банить пользователя в чате
    через команду
    """
    if message.chat.type != 'private':
        admin_author = await check_user_is_admin(message)
        print(f"{admin_author=}")
        if admin_author and message.reply_to_message:
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id
            )



