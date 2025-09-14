import asyncio
from aiogram import F, Bot, Dispatcher
from aiogram.types import Message, ChatPermissions
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

#Я ПИДОРАС

bot = Bot(token="7151855743:AAFWpJDdnotf6gWtLtKkMHrSD57hQvrKShA", default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

list_sosal = ["сосал", "сосал?", "sosal", "/sosal"]

@dp.message(F.text.lower().in_(list_sosal))
async def any_message(message: Message):
    await message.answer_sticker("CAACAgIAAxkBAAERoddoqZgKFpEAAQsmGDwVOz_kSVSoW24AAg1bAAKFO_FJHbT9d73-uQQ2BA")   

# @dp.message(F.text == "/info")
# async def any_message(message: Message):
#     member = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
#     await message.answer(member)  

@dp.message(F.text == "/info")
async def get_user_info(message: Message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user
    else:
        user = message.from_user

    info_text = (
        f"• ID: <code>{user.id}</code>\n"
        f"• Имя: {user.first_name}\n"
        f"• Фамилия: {user.last_name or '—'}\n"
        f"• Username: @{user.username or 'не указан'}\n"

    )

    await message.reply(info_text, parse_mode="HTML")


async def Mute(boolean: bool):
    mute = ChatPermissions(
            can_send_messages=boolean,
            can_send_media_messages=boolean,
            can_send_other_messages=boolean,
            can_add_web_page_previews=boolean,
            can_send_polls=boolean,
            can_change_info=boolean,
            can_invite_users=boolean,
            can_pin_messages=boolean
)
    return mute    

async def check_status(message: Message, stat: str, reply: bool):
    if reply == True:
        member = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
    else:
        member = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)

    if member.status == stat:
        return True
    else:
        return False
    

        
@dp.message(F.text == "мут")
async def any_message(message: Message):
    try:
        if not message.reply_to_message:
            await message.reply("Чтобы замьютить, ответь на сообщение пользователя.")
            return
        if await check_status(message, "administrator", False) or await check_status(message, "creator", False):
            if message.reply_to_message.from_user.id == message.from_user.id:
                await message.reply("Вы не можете замьютить себя")     
            elif message.reply_to_message.from_user.is_bot:
                await message.reply("Вы не можете замьютить бота")
            elif await check_status(message, "restricted", True):
                await message.reply("Пользователь уже замьючен") 
            else:
                await bot.restrict_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id, permissions=await Mute(False))
                await message.reply(f"{message.reply_to_message.from_user.mention_html()} заткнул ебальник")
        else:
            await message.reply("У вас недостаточно прав")       
    except Exception as e:
        await message.reply(f"Произошла ошибка:\n{e}")



@dp.message(F.text == "размут")
async def any_message(message: Message):
    try:   
        if await check_status(message, "administrator", False) or await check_status(message, "creator", False):
            if await check_status(message, "restricted", True) == False:
                await message.reply("Пользователь не был замьючен") 
            else:
                await bot.restrict_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id, permissions=await Mute(True))
                await message.reply(f"{message.reply_to_message.from_user.mention_html()} вернул себе право голоса")    
        else:
            await message.reply("У вас недостаточно прав")       
    except Exception as e:
        await message.reply(f"Произошла ошибка:\n{e}")



# with open('admin_roles.json', 'w') as file:
#     data = json.loads(file)
#     json.dump(data, file)

# with open('admin_roles.json', 'r') as file:
#     data = json.loads(file)

# @dp.message(F.text == "размут1")
# async def any_message(message: Message):
#     await bot.restrict_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id, permissions=await Mute(True))
#     await message.reply(f"{message.reply_to_message.from_user.mention_html()} вернул себе право голоса")    
       

# @dp.message(F.text == "бан")
# async def any_message(message: Message): 
#     try:
#         if message.reply_to_message.from_user.id == message.from_user.id:
#             await message.reply("Вы не можете забанить себя")     
#         elif await check_admin(message):
#             if message.reply_to_message.from_user.is_bot:
#                 await message.reply("Вы не можете забанить бота")
#             elif await check_ban(message):
#                 await message.reply("Пользователь уже забанен") 
#             elif await check_reply_admin(message) and await check_creator(message) == False:
#                 await message.reply("У вас недостаточно прав")
#             else:
#                 await bot.ban_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
#                 await message.reply(f"{message.reply_to_message.from_user.mention_html()} забанен нахуй")           
#     except:
#         await message.reply("Произошла неожиданная ошибка")

# @dp.message(F.text == "разбан")
# async def any_message(message: Message): 
#     try:  
#         if await check_admin(message):
#             if await check_unban(message):
#                 await message.reply("Пользователь не был забанен") 
#             elif await check_reply_admin(message) and await check_creator(message) == False:
#                 await message.reply("У вас недостаточно прав")
#             else:
#                 await bot.unban_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
#                 inv= await bot.create_chat_invite_link(chat_id=message.chat.id, member_limit=1)
#                 await message.reply(f"{message.reply_to_message.from_user.mention_html()} может вернуться назад\nСсылка: {inv.invite_link}")          
#     except:
#         await message.reply("Произошла неожиданная ошибка")



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())