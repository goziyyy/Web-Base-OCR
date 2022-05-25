print("Starting Telegram-Image-Scraper...")
from pyrogram import Client, filters
import config

import os
import cv2
import pytesseract

os.environ["TESSDATA_PREFIX"] = "./lang/"

pytesseract_config=('-l eng --oem 1 --psm 3')

api_id = int(os.environ.get("API_ID"))
api_hash = str(os.environ.get("API_HASH"))
session_name = str(os.environ.get("SESSION_NAME"))
bot_token = str(os.environ.get("BOT_TOKEN"))

app = Client(
    session_name,
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

print("Telegram-Image-Scraper connected successfully!")

@app.on_message(filters.photo)
async def scrape_text(client, message):
    await message.download("temp.jpg")
    img = cv2.imread('./downloads/temp.jpg')
    text = pytesseract.image_to_string(img, config=pytesseract_config)
    print(text)
    await message.reply(text)


app.run()