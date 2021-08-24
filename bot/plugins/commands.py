#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error



db = Database()

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
        caption = ("<code>" + file_name + """</code>\n\n<b>🔰👉കടുതൽ സിനിമകൾക്കും മറ്റു വിവരങ്ങൾക്കുമായി ഞങ്ങളുടെ ഗ്രൂപ്പിൽ ജോയിൻ ചെയ്യൂ\n\n\n🌟༺ ──•◈•─ ─•◈•──༻🌟➧\n\n@TELSABOTS\n➧ @FILIMSMOVIE </b>""")
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
