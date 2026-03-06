from pyrogram import filters
from pyrogram.types import Message

from AviaxMusic import app
from AviaxMusic.core.call import Aviax


@app.on_message(filters.video_chat_started, group=20)
async def vc_started(_, message: Message):
    pass  # VC start pe kuch nahi — fresh join khud hoga


@app.on_message(filters.video_chat_ended, group=30)
async def vc_ended(_, message: Message):
    print(f"VC ENDED EVENT: {message.chat.id}")  # DEBUG
    await Aviax.stop_stream_force(message.chat.id)
