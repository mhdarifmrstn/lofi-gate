from pyrogram import Client, idle
from pytgcalls.types import MediaStream
from pytgcalls import PyTgCalls
from dotenv import load_dotenv
from mutagen.mp3 import MP3
from asyncio import get_event_loop
from os import getenv
from extra import get_random_file
from time import sleep

load_dotenv()

api_id = int(getenv("API_ID"))
api_hash = getenv("API_HASH")
string_session = getenv("STRING_SESSION")
bot_token = getenv("BOT_TOKEN")
user_account = Client("lofi_gate", api_id=api_id, api_hash=api_hash, session_string=string_session)
call_account = PyTgCalls(user_account)
loop = get_event_loop()
chat_ids = list(map(int, getenv("CHAT_IDS").split()))
music_dir = './musics/'

async def init():
  await user_account.start()
  user = await user_account.get_me()
  print(f"App started as {user.first_name}")
  async for dialog in user_account.get_dialogs(): pass
  await call_account.start()

  while True:
    random_song = music_dir + get_random_file(music_dir)
    audio = MP3(random_song)
    duration = audio.info.length
    
    for chat_id in chat_ids:
      await call_account.play(chat_id, MediaStream(random_song))
    sleep(duration)

loop.run_until_complete(init())
