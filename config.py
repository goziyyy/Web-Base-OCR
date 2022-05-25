import os

config = {
    "API_ID": "INSERT API_ID HERE",
    "API_HASH": "INSERT API_HASH HERE",
    "SESSION_NAME": "photobot",
    "BOT_TOKEN": "INSERT BOT TOKEN HERE"
}

os.environ.setdefault("API_ID", config["API_ID"])
os.environ.setdefault("API_HASH", config["API_HASH"])
os.environ.setdefault("SESSION_NAME", config["SESSION_NAME"])
os.environ.setdefault("BOT_TOKEN", config["BOT_TOKEN"])