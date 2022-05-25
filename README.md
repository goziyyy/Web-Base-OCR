# Telegram-Image-Scraper
A Telegram Bot that allows you to scrape text from images.

## Install global dependencies
    
### Debian Based
    apt install python3 tesseract-ocr python3-opencv -y
    
### Arch based
    pacman -S python3 tesseract opencv


## Installation of Python dependencies
  
 To install python dependencies, simply run pip
 
    pip install pyrogram tgcrypto pytesseract opencv-python

          
## Installation
Clone this repository using

    git clone https://github.com/xFr33z3/Telegram-Image-Scraper.git

Change folder to Telegram-Image-Scraper directory

    cd Telegram-Image-Scraper
    
Go to https://my.telegram.org/, log in, and in API Development Tools section, create new application. You will retreive 2 values named API_ID and API_HASH.
Then open Telegram and create a new bot using https://t.me/BotFather, and get the BOT_TOKEN value.
So edit the file <code>config.py</code>:

    config = {
    "API_ID": "INSERT API_ID HERE",
    "API_HASH": "INSERT API_HASH HERE",
    "SESSION_NAME": "photobot",
    "BOT_TOKEN": "INSERT BOT TOKEN HERE"
    }
    
Run with

    python3 main.py
