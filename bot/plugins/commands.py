#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # pylint: disable=import-error
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, UsernameNotOccupied, ChatAdminRequired, PeerIdInvalid
import asyncio
from bot.database import Database 
from config import Config
import aiofiles
from database import Database


db = Database()

@Bot.on_message(filters.command("start") & filters.private)
async def start(bot, cmd):
	if not await db.is_user_exist(cmd.from_user.id):
		await db.add_user(cmd.from_user.id)
		await bot.send_message(
		    Config.LOG_CHANNEL,
		    f"#NEW_USER: \n\nNew User [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id}) started @{BOT_USERNAME} !!"
		)
	usr_cmd = cmd.text.split("_")[-1]
	if usr_cmd == "/start":
		if Config.UPDATES_CHANNEL:
			invite_link = await bot.create_chat_invite_link(int(Config.UPDATES_CHANNEL))
			try:
				user = await bot.get_chat_member(int(Config.UPDATES_CHANNEL), cmd.from_user.id)
				if user.status == "kicked":
					await bot.send_message(
						chat_id=cmd.from_user.id,
						text="You are Banned😛. Contact my [Support Group](https://t.me/TeleRoid14).",
						parse_mode="markdown",
						disable_web_page_preview=True
					)
					return
			except UserNotParticipant:
				await bot.send_message(
					chat_id=cmd.from_user.id,
					text="**𝐏𝐥𝐞𝐚𝐬𝐞 𝐉𝐨𝐢𝐧 𝐌𝐲 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐭𝐨 𝐮𝐬𝐞 𝐭𝐡𝐢𝐬 𝐁𝐨𝐭!**\n\n𝐃𝐮𝐞 𝐭𝐨 𝐎𝐯𝐞𝐫𝐥𝐨𝐚𝐝, 𝐎𝐧𝐥𝐲 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐒𝐮𝐛𝐬𝐜𝐫𝐢𝐛𝐞𝐫𝐬 can use the Bot!",
					reply_markup=InlineKeyboardMarkup(
						[
							[
								InlineKeyboardButton("⭕ 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ⭕", url=invite_link.invite_link)
							],
							[
								InlineKeyboardButton("🔄 𝐑𝐞𝐟𝐫𝐞𝐬𝐡 🔄", callback_data="refreshmeh")
							]
						]
					),
					parse_mode="markdown"
				)
				return
			except Exception:
				await bot.send_message(
					chat_id=cmd.from_user.id,
					text="Something went Wrong. Contact my [🛑 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 🛑](https://t.me/TeleRoid14).",
					parse_mode="markdown",
					disable_web_page_preview=True
				)
				return
		await cmd.reply_text(
			HOME_TEXT.format(cmd.from_user.first_name, cmd.from_user.id),
			parse_mode="Markdown",
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("🛑 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 🛑", url="https://t.me/TeleRoid14"),
						InlineKeyboardButton("⭕ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ⭕", url="https://t.me/TeleRoidGroup")
					],
					[
						InlineKeyboardButton("👥 𝐀𝐛𝐨𝐮𝐭 ", callback_data="aboutbot"),
						InlineKeyboardButton("👨‍🔧 𝐃𝐞𝐯 ", callback_data="aboutdevs")
					], 
                                        [
						InlineKeyboardButton("🌐 𝐆𝐢𝐭𝐡𝐮𝐛 ", url="https://GitHub.com/PredatorHackerzZ"),
						InlineKeyboardButton("📢 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲", url="https://t.me/MoviesFlixers_DL")
					]
				]
			)
		)
	else:
		if Config.UPDATES_CHANNEL:
			invite_link = await bot.create_chat_invite_link(int(Config.UPDATES_CHANNEL))
			try:
				user = await bot.get_chat_member(int(Config.UPDATES_CHANNEL), cmd.from_user.id)
				if user.status == "kicked":
					await bot.send_message(
						chat_id=cmd.from_user.id,
						text="𝐒𝐨𝐫𝐫𝐲 𝐒𝐢𝐫, 𝐘𝐨𝐮 𝐚𝐫𝐞 𝐁𝐚𝐧𝐧𝐞𝐝 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞. 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐦𝐲 [🛑 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩 🛑](https://t.me/TeleRoid14).",
						parse_mode="markdown",
						disable_web_page_preview=True
					)
					return
			except UserNotParticipant:
				file_id = int(usr_cmd)
				await bot.send_message(
					chat_id=cmd.from_user.id,
					text="**𝐏𝐥𝐞𝐚𝐬𝐞 𝐉𝐨𝐢𝐧 𝐌𝐲 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞!**\n\n𝐃𝐮𝐞 𝐭𝐨 𝐎𝐯𝐞𝐫𝐥𝐨𝐚𝐝, 𝐎𝐧𝐥𝐲 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐒𝐮𝐛𝐬𝐜𝐫𝐢𝐛𝐞𝐫𝐬 𝐜𝐚𝐧 𝐮𝐬𝐞 𝐭𝐡𝐞 𝐁𝐨𝐭!",
					reply_markup=InlineKeyboardMarkup(
						[
							[
								InlineKeyboardButton("𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url=invite_link.invite_link)
							],
							[
								InlineKeyboardButton("🔄 𝐑𝐞𝐟𝐫𝐞𝐬𝐡 / 𝐓𝐫𝐲 𝐀𝐠𝐚𝐢𝐧", url=f"https://telegram.dog/{BOT_USERNAME}?start=TeleRoid14_{file_id}")
							]
						]
					),
					parse_mode="markdown"
				)
				return
			except Exception:
				await bot.send_message(
					chat_id=cmd.from_user.id,
					text="Something went Wrong. Contact my [🛑 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩 🛑 ](https://t.me/TeleRoid14).",
					parse_mode="markdown",
					disable_web_page_preview=True
				)
				return
		try:
			file_id = int(usr_cmd)
			send_stored_file = await bot.copy_message(chat_id=cmd.from_user.id, from_chat_id=DB_CHANNEL, message_id=file_id)
			await send_stored_file.reply_text(f"**Here is Sharable Link of this file:** https://telegram.dog/{BOT_USERNAME}?start=TeleRoid14_{file_id}\n\n__To Retrive the Stored File, just open the link!__", disable_web_page_preview=True, quote=True)
		except Exception as err:
			await cmd.reply_text(f"Something went wrong!\n\n**Error:** `{err}`")
            
            return

    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
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
                                    'Developers', url="https://t.me"
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
                                    'Developers', url="https://t.me"
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
                                    'Developers', url="https://t.me"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('🤔 Help', callback_data='help'),
        InlineKeyboardButton('🤖 About', callback_data='about')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
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
        InlineKeyboardButton('Home 🏠', callback_data='start'),
        InlineKeyboardButton('About🤖', callback_data='about')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
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
        InlineKeyboardButton('Home 🤖', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
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
