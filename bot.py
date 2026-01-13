import os
import asyncio
import random
from pyrogram import Client

API_ID = 39887299
API_HASH = "cec76ec22570e488c62e3718bc81c6f1"
STICKER_FOLDER = "stickers"
TARGET_BOT = "Stickers"
DELAY = 2.5

EMOJIS = [
    "😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰",
    "😘", "😗", "😙", "😚", "😋", "😛", "😝", "😜", "🤪", "🤨", "🧐", "🤓", "😎", "🥸", "🤩", "🥳",
    "😏", "😒", "😞", "😔", "😟", "😕", "🙁", "☹️", "😣", "😖", "😫", "😩", "🥺", "😢", "😭", "😤",
    "😠", "😡", "🤬", "🤯", "😳", "🥵", "🥶", "😱", "😨", "😰", "😥", "😓", "🤗", "🤔", "🫣", "🤭",
    "🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐨", "🐯", "🦁", "🐮", "🐷", "🐸", "🐵", "🙈",
    "🙉", "🙊", "🐔", "🐧", "🐦", "🐤", "🐣", "🦆", "🦅", "🦉", "🦇", "🐺", "🐗", "🐴", "🦄", "🐝",
    "🎉", "🎊", "🎈", "🎁", "🪅", "💌", "💣", "💥", "🧨", "🪄", "🧸", "🪆", "🛍️", "📦", "🗿", "🪐",
    "🌈", "🔥", "🌟", "⭐", "⚡", "❄️", "💧", "💦", "🌊", "🍀", "🍄", "🌺", "🌸", "🪷", "🌻", "🌹",
    "👍", "👎", "👌", "✌️", "🤞", "🤟", "🤘", "🤙", "👊", "✊", "👏", "🙌", "👐", "🤲", "🙏", "🤝",
    "🍎", "🍉", "🍓", "🍒", "🍍", "🥭", "🍑", "🍌", "🍇", "🥝", "🥥", "🍅", "🍆", "🌽", "🌶️", "🥕",
    "🧄", "🧅", "🥔", "🥐", "🍞", "🧀", "🍕", "🍔", "🍟", "🌭", "🥪", "🌮", "🌯", "🥗", "🍿", "🥤"
]

async def send_stickers():
    app = Client("stickers", api_id=API_ID, api_hash=API_HASH)
    await app.start()

    if not os.path.exists(STICKER_FOLDER):
        print(f"❌ Folder not found: {STICKER_FOLDER}")
        return

    sticker_files = [f for f in os.listdir(STICKER_FOLDER) if f.lower().endswith(".webp")]
    if not sticker_files:
        print("❌ No .webp stickers found.")
        return

    random.shuffle(sticker_files)
    print(f"🚀 Sending {len(sticker_files)} stickers to @{TARGET_BOT}...")

    for i, sticker_name in enumerate(sticker_files):
        path = os.path.join(STICKER_FOLDER, sticker_name)
        try:
            await app.send_document(chat_id=TARGET_BOT, document=path)
            print(f"✅ Sent sticker: {sticker_name}")
            await asyncio.sleep(DELAY)
            emoji = EMOJIS[i % len(EMOJIS)]
            await app.send_message(chat_id=TARGET_BOT, text=emoji)
            print(f"✨ Sent emoji: {emoji}")
            await asyncio.sleep(DELAY)
        except Exception as e:
            print(f"❌ Failed to send {sticker_name}: {e}")

    print("🎉 All stickers and emojis sent!")
    await app.stop()

if __name__ == "__main__":
    asyncio.run(send_stickers())