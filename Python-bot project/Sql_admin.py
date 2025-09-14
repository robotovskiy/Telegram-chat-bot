import sqlite3
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import Command

import asyncio
from aiogram import F, Bot, Dispatcher
from aiogram.types import Message, ChatPermissions, User
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

BOT_TOKEN = "7151855743:AAFWpJDdnotf6gWtLtKkMHrSD57hQvrKShA"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

DB_NAME = "users.db"

def init_db():
    with sqlite3.connect(DB_NAME) as c:
        c.execute("""
            CREATE TABLE IF NOT EXISTS admin_roles (     
                username text,
                can_pin_messages text,
                can_delete_messages text,
                can_mute text,
                can_ban text
            )
        """)

def can_make(pin: bool, delete: bool, mute: bool, ban: bool):
    can = [pin, delete, mute, ban]
    return can

# def save_user(user: User):
#     with sqlite3.connect(DB_NAME) as c:
#         c.execute("""
#             INSERT OR REPLACE INTO users (user_id, username, first_name, last_name)
#             VALUES (?, ?, ?, ?)
#         """, (
#             user.id,
#             user.username,
#             user.first_name,
#             user.last_name
#         ))



# def give_admin_role(user: User, name: str, pin: bool, delete: bool, mute: bool, ban: bool):
#     with sqlite3.connect(DB_NAME) as c:
#         c.execute("""
#             INSERT OR REPLACE INTO admin_roles (can_pin_messages, can_delete_messages, can_mute, can_ban)
#             VALUES (?, ?, ?, ?)
#         """, (
#             pin,
#             delete,
#             mute,
#             ban
#         ))
#         c.execute("""
#             INSERT OR REPLACE INTO users (admin_role)
#             VALUES (?)
#         """, (name))


@dp.message(F.text.startswith("Сделать роль администратора"))
async def cmd_get(message: Message):
    # await message.reply(f"пошел нахуй")

    data = message.text

    # str_data = str(F.text)

    admin_data_list = ["Название", "Можно закреплять сообщения", "Можно удалять сообщения", "Можно банить", "Можно мутить"]

    res = data.split("\n")

    num = 0
    for i in res[1:]:
        
        if i.startswith(admin_data_list[num]):
            # await message.reply(f"{i} начинается с {admin_data_list[num]}")
            el_list = i.split()
            hui = admin_data_list[num].split()
            if len(el_list) == len(hui) + 1:
                await message.reply(f"работаем дальше")
            elif len(el_list) > len(hui) + 1:
                await message.reply(f"много слов")
            else:
                await message.reply(f"мало слов")

            # await message.reply(f"{len(el_list)} и {len(hui)}")
        num += 1




    # name = name
    # list = list
    # make_admin_role(name, list)


# @dp.message(F.text == "Сделать роль администратора")
# async def cmd_get(message: Message):
#     user = message.reply_to_message.from_user
#     await message.reply(f"Придуймате название для роли")




    # user_id = message.reply_to_message.from_user.id
    
    # with sqlite3.connect(DB_NAME) as c:
    #     row = c.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
    # if row:
    #     _, username, first_name, last_name = row
    #     await message.reply(
    #         f"🔍 Пользователь в базе:\n"
    #         f"• Логин: @{username or 'не указан'}\n"
    #         f"• Имя: {first_name} {last_name or ''}"
    #     )
    # else:
    #     await message.reply("Пользователя нет в базе. Используй /save")



def make_admin_role(name: str, can: list):
    with sqlite3.connect(DB_NAME) as c:
        c.execute("""
            INSERT OR REPLACE INTO admin_roles (can_pin_messages, can_delete_messages, can_mute, can_ban)
            VALUES (?, ?, ?, ?)
        """, (
            can[0],
            can[1],
            can[2],
            can[3]
        ))
        # c.execute("""
        #     INSERT OR REPLACE INTO users (admin_role)
        #     VALUES (?)
        # """, (name))



# def get_all():
#     with sqlite3.connect(DB_NAME) as c:
#         mas = c.execute("SELECT * FROM users")
#         return mas



# @dp.message(F.text == "save")
# async def cmd_save(message: Message):
#     user = message.reply_to_message.from_user
#     save_user(user)

#     await message.reply(
#         f"Загрузка завершена.\n"
#         f"• ID: {user.id}\n"
#         f"• Логин: @{user.username or 'не указан'}\n"
#         f"• Имя: {user.first_name} {user.last_name or ''}"
#     )

# @dp.message(F.text == "get")
# async def cmd_get(message: Message):
#     user_id = message.reply_to_message.from_user.id
    
#     with sqlite3.connect(DB_NAME) as c:
#         row = c.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
#     if row:
#         _, username, first_name, last_name = row
#         await message.reply(
#             f"🔍 Пользователь в базе:\n"
#             f"• Логин: @{username or 'не указан'}\n"
#             f"• Имя: {first_name} {last_name or ''}"
#         )
#     else:
#         await message.reply("Пользователя нет в базе. Используй /save")



# @dp.message(F.text == "input")
# async def cmd_get(message: Message):
#     # user_id = message.reply_to_message.from_user.id

#     # with sqlite3.connect(DB_NAME) as conn:
#     #     row = conn.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()

#     # if row:
#     #     _, username, first_name, last_name = row
#     #     await message.reply(
#     #         f"🔍 Это в базе:\n"
#     #         f"• Логин: @{username or 'не указан'}\n"
#     #         f"• Имя: {first_name} {last_name or ''}"
#     #     )
#     # else:
#     mas = get_all()
#     for i in mas:
#         await message.answer(str(i))

# Запуск бота
async def main():
    init_db()  # создаём таблицу
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())