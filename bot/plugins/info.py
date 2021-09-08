from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('❤️SUBSCRIBE❤️', url='https://youtu.be/e7wUj5uyRyo')
        ],[
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )

@Client.on_message(filters.command(["info", "information"]), group=1)
async def information(bot, update):
    if (not update.reply_to_message) and ((not update.forward_from) or (not update.forward_from_chat)):
        info = user_info(update.from_user)
    elif update.reply_to_message and update.reply_to_message.forward_from:
        info = user_info(update.reply_to_message.forward_from)
    elif update.reply_to_message and update.reply_to_message.forward_from_chat:
        info = chat_info(update.reply_to_message.forward_from_chat)
    elif (update.reply_to_message and update.reply_to_message.from_user) and (not update.forward_from or not update.forward_from_chat):
        info = user_info(update.reply_to_message.from_user)
    else:
        return
    try:
        await update.reply_text(
            text=info,
            reply_markup=BUTTONS,
            disable_web_page_preview=True,
            quote=True
        )
    except Exception as error:
        await update.reply_text(error)

def user_info(user):
    text = "<b>YOUR DETAILS:</b>\n"
    text += f"\n<b>FIRST NAME:</b> `{user.first_name}`"
    text += f"\n<b>LAST NAME:</b> `{user.last_name}`" if user.last_name else ""
    text += f"\n<b>YOUR ID:</b> `{user.id}`"
    text += f"\n<b>YOUR USERNAME:</b> @{user.username}" if user.username else ""
    text += f"\n<b>YOUR LINK :</b>{user.mention}" if user.username else ""
    text += f"\n<b>DC ID:</b>`{user.dc_id}`" if user.dc_id else ""
    text += f"\n<b>STATUS:</b> {user.status}" if user.status else ""
    text += f"\n\n<b>BOT RESTARTED ON 09 September 2021 12:16  AM (INDIAN TIME ZONE)</b>\n"
    text += f"\n\n<b>JOIN @TELSABOTS</b>"
    return text


def chat_info(chat):
    text = "<b>Chat Details</b>\n" 
    text += f"\n<b>Title:</b>`{chat.title}`"
    text += f"\n<b>Chat ID:</b> `{chat.id}`"
    text += f"\n<b>Username:</b> @{chat.username}" if chat.username else ""
    text += f"\n<b>Type:</b> `{chat.type}`"
    text += f"\n<b>DC ID:</b> `{chat.dc_id}`"
    text += f"\n<b>Is Creator:</b> True" if chat.is_creator else ""
    text += f"\n\n<b>JOIN @TELSABOTS</b>"
    return text
