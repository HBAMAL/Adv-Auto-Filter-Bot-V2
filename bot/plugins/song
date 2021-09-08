import os 
from pyrogram import Client, filters
import asyncio
from youtube_dl import YoutubeDL
import requests
import aiohttp
import youtube_dl
from datetime import datetime
import time
from youtube_search import YoutubeSearch
from opencc import OpenCC
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputTextMessageContent, Message

@Client.on_message(filters.command('music'))
def song(client, message):

    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply('SEARCHING🧐')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)

        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        m.edit(
            "**NOTHING FOUND.\n\nCHECK SPELLING**"
        )
        print(str(e))
        return
    m.edit("**📥DOWNLOADING📥**")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f' **SONG🎧**: [{title[:35]}]({link})\n**DURATION⏰**: `{duration}`\n**VIEWS👀**: `{views}`\n**JOIN❤️** @TELSABOTS'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        s = message.reply_audio(audio_file, caption=rep, thumb=thumb_name, parse_mode='md', title=title, duration=dur)
        m.delete()
        


    except Exception as e:
        m.edit('**SOMETHING WENT WRONG**')
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
