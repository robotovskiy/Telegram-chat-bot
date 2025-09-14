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
            CREATE TABLE IF NOT EXISTS users (
                user_id integer primary key,
                username text,
                first_name text,
                last_name text,
                admin_role text
            )
        """)

def save_user(user: User):
    with sqlite3.connect(DB_NAME) as c:
        c.execute("""
            INSERT OR REPLACE INTO users (user_id, username, first_name, last_name)
            VALUES (?, ?, ?, ?)
        """, (
            user.id,
            user.username,
            user.first_name,
            user.last_name
        ))

# def get_all():
#     with sqlite3.connect(DB_NAME) as c:
#         mas = c.execute("SELECT * FROM users")
#         return mas

@dp.message(F.text == "save")
async def cmd_save(message: Message):
    user = message.reply_to_message.from_user
    save_user(user)

    await message.reply(
        f"Загрузка завершена.\n"
        f"ID: {user.id}\n"
        f"Логин: @{user.username or 'не указан'}\n"
        f"Имя: {user.first_name} {user.last_name or ''}"
    )

@dp.message(F.text == "get")
async def cmd_get(message: Message):
    user_id = message.reply_to_message.from_user.id
    
    with sqlite3.connect(DB_NAME) as c:
        row = c.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
    if row:
        _, username, first_name, last_name = row
        await message.reply(
            f"Пользователь в базе:\n"
            f"Логин: @{username or 'не указан'}\n"
            f"Имя: {first_name} {last_name or ''}"
        )
    else:
        await message.reply("Пользователя нет в базе. Используй /save")



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