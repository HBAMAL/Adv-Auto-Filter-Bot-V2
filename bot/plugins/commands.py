from bot import UPDATE_CHANNEL 
from pyrogram.errors import UserNotParticipant
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error



db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("😔 Sorry Dude, You are **🅱︎🅰︎🅽︎🅽︎🅴︎🅳︎ 🤣🤣🤣**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="<b>🥴HEY U STILL DON'T JOINED MY CHANNEL 🤭.\n\n😊 JOIN MY CHANNEL THEN ONLY U CAN USE ME 😊</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="😊JOIN NOW😊", url=f"https://t.me/{UPDATE_CHANNEL}")]
              ])
            )
            return
        except Exception:
            await update.reply_text(f"<b>This bot should be the admin on your update channel</b>\n\n<b>💢 ഈ ചാനലിൽ  @{UPDATE_CHANNEL} ബോട്ടിനെ അഡ്മിൻ ആക്. എന്നിട്ട് /start കൊടുക്</b>")
            return  
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
                        ],
                        [
                            InlineKeyboardButton
                                (
                                    '🧑🏼‍💻DEV🧑🏼‍💻', url="https://t.me/alluaddict"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            await update.bot.send_video(
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
                        ],
                        [
                            InlineKeyboardButton
                                (
                                    '🧑🏼‍💻DEV🧑🏼‍💻', url="https://t.me/alluaddict"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await update.bot.send_audio(
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
                        ],
                        [
                            InlineKeyboardButton
                                (
                                    '🧑🏼‍💻DEV🧑🏼‍💻', url="https://t.me/alluaddict"
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
    
    await bot.send_photo(
        chat_id=update.chat.id,
        photo="https://telegra.ph/file/cd90aad8b40af60b96aa8.jpg",
        caption=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
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
        reply_to_message_id=update.message_id
    )
@Client.on_message(filters.command(["source"]) & filters.private, group=1)
async def source(bot, update):
    buttons = [[
        InlineKeyboardButton('🔰CHANNEL🔰', url='t.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='t.me/alluaddict')
    ],[
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')     
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_sticker(
        chat_id=update.chat.id,
        sticker='CAACAgUAAxkBAAPFYSUyZ8rYvkPnNe-fsaegX9DUe-oAAo8AAxgQCD12sH8mfviJrx4E',
        reply_markup=reply_markup,
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
