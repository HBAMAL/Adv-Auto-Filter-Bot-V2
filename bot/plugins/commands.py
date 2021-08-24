#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram.errors import UserNotParticipant
import os
import datetime
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error



db = Database()

@Client.on_message(filters.private & filters.incoming)
async def force_sub(c, m):
    if Config.FORCE_SUB:
        try:
            chat = await c.get_chat_member(Config.FORCE_SUB, m.from_user.id)
            if chat.status=='kicked':
                return await m.reply_text('Hai you are kicked from my updates channel. So, you are not able to use me',  quote=True)

        except UserNotParticipant:
            button = [[InlineKeyboardButton('💫Join Updates Channel💫', url=f"https://t.me/{Config.FORCE_SUB}")]]
            markup = InlineKeyboardMarkup(button)
            return await m.reply_text(text="**You Must Join My Updates Channel To Use Me**", parse_mode='markdown', reply_markup=markup, quote=True)

        except ChatAdminRequired:
            logger.warning(f"Make me admin in @{Config.FORCE_SUB}")
            if m.from_user.id in Config.AUTH_USERS:
                return await m.reply_text(f"Make me admin in @{Config.FORCE_SUB}")

        except UsernameNotOccupied:
            logger.warning("The forcesub username was Incorrect. Please give the correct username.")
            if m.from_user.id in Config.AUTH_USERS:
                return await m.reply_text("The forcesub username was Incorrect. Please give the correct username.")

        except Exception as e:
            if "belongs to a user" in str(e):
                logger.warning("Forcesub username must be a channel username Not yours or any other users username")
                if m.from_user.id in Config.AUTH_USERS:
                    return await m.reply_text("Forcesub username must be a channel username Not yours or any other users username")
            logger.error(e)
            return await m.reply_text("Some thing went wrong. CONTACT [🧑🏼‍💻DEV🧑🏼‍💻](https://t.me/alluaddict)", disable_web_page_preview=True, quote=True)

    await m.continue_propagation()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        caption = ("<code>" + file_name + """</code>\n\n<b>🔰👉കടുതൽ സിനിമകൾക്കും മറ്റു വിവരങ്ങൾക്കുമായി ഞങ്ങളുടെ ഗ്രൂപ്പിൽ ജോയിൻ ചെയ്യൂ\n\n\n🌟༺ ──•◈•─ ─•◈•──༻🌟\n\n➧@TELSABOTS\n➧ @FILIMSMOVIE </b>""")
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = caption,
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '❤️JOIN❤️', url="https://t.me/TELSABOTS"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '❤️JOIN❤️', url="https://t.me/TELSABOTS"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '❤️JOIN❤️', url="https://t.me/TELSABOTS"
                                )
                        ]
                    ]
                )
            )

       else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('🔰CHANNEL🔰', url='t.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='t.me/alluaddict')
    ],[
        InlineKeyboardButton('🆘HELP🆘', callback_data='help'),
        InlineKeyboardButton('☺️ABOUT☺️', callback_data='about')
    ],[
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')     
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('🔰CHANNEL🔰', url='t.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='t.me/alluaddict')
    ],[
        InlineKeyboardButton('🏡HOME 🏡', callback_data='start'),
        InlineKeyboardButton('☺️ABOUT☺️', callback_data='about')
    ],[
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('🔰CHANNEL🔰', url='t.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='t.me/alluaddict')
    ],[
        InlineKeyboardButton('🏡HOME 🏡', callback_data='start'),
        InlineKeyboardButton('☺️ABOUT☺️', callback_data='about')
    ],[
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')     
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
