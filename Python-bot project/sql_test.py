import asyncio
from aiogram import F, Bot, Dispatcher
from aiogram.types import Message, ChatPermissions
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
import sqlite3

bot = Bot(token="7151855743:AAFWpJDdnotf6gWtLtKkMHrSD57hQvrKShA", default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()



# async def get_user_info(message: Message):
#     if message.reply_to_message:
#         user = message.reply_to_message.from_user
#     else:
#         user = message.from_user

#     # info_text = (
#     #     f"• ID: <code>{user.id}</code>\n"
#     #     f"• Имя: {user.first_name}\n"
#     #     f"• Фамилия: {user.last_name or '—'}\n"
#     #     f"• Username: @{user.username or 'не указан'}\n"

#     # )
#     user_data = [user.id, user.first_name, user.last_name, user.username]
#     return user_data

#     # await message.reply(info_text, parse_mode="HTML")




dbase = sqlite3.connect('data.db')


cur = dbase.cursor()
# cur.execute("""CREATE TABLE articles 
#             (ID int, 
#             Username text,
#             First_name text,
#             Last_name text)
# """)

# cur.execute("INSERT INTO articles VALUES(12345, 'SuperGlebik123', 'Глеб', 'Хидоятов')")
# cur.execute("INSERT INTO articles VALUES(54321, 'MegaSyasik321', 'Сяся', 'Глущенко')")


cur.execute("""CREATE TABLE UpRoles 
            (ID int, 
            Username text,
            First_name text,
            Last_name text)
""")


cur.execute("SELECT * FROM articles")
#WHERE
#ORDER BY
print (cur.fetchall())

#rowid
# print (cur.fetchall())
# print (cur.fetchmany(1))
# print (cur.fetchone())

# mas = cur.fetchall()

# for i in mas:
#     print(i[1] + "\n")


# cur.execute("DELETE FROM articles")
# print (cur.fetchall())

# cur.execute("UPDATE articles SET")



dbase.commit()

dbase.close()

# @dp.message(F.text == "занести")
# async def any_message(message: Message):
#     await get_user_info(message)



