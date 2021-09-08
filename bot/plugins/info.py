from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



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
    text = "--**User Details:**--\n"
    text += f"\n**First Name:** `{user.first_name}`"
    text += f"\n**Last Name:** `{user.last_name},`" if user.last_name else ""
    text += f"\n**User Id:** `{user.id}`"
    text += f"\n**Username:** @{user.username}" if user.username else ""
    text += f"\n**User Link:** {user.mention}" if user.username else ""
    text += f"\n**DC ID:** `{user.dc_id}`" if user.dc_id else ""
    text += f"\n**Status:** {user.status}" if user.status else ""
    text += f"\n\nJOIN TELSABOTS"
    return text


def chat_info(chat):
    text = "--**Chat Details**--\n" 
    text += f"\n**Title:** `{chat.title}`"
    text += f"\n**Chat ID:** `{chat.id}`"
    text += f"\n**Username:** @{chat.username}" if chat.username else ""
    text += f"\n**Type:** `{chat.type}`"
    text += f"\n**DC ID:** `{chat.dc_id}`"
    text += f"\n**Is Creator:** True" if chat.is_creator else ""
    text += f"\n\nJOIN TELSABOTS"
    return text
