from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID", "25529098")
APP_HASH = os.environ.get("APP_HASH", "d0a0078f95340f9af195ecf8821db9f1")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "rithonbot")
session = os.environ.get("TERMUX", "AgADKFifKED3-a7xQUCzU-H-Xsu8OE-zf26yDuHLRNsxQKNCbrRixFRMGOatDi_XCgSx9nAZ-aB8LtTBbUkRru5b6WIhNLjK4peQFf1Qic7Zb36hb3ufylbi7YyBdwKV7IprqCOy0g5n6PumdetnbpIn-pnl5QuqXGF9sR5e-nWrfseX3T74RihNLmS6TnAY8S46civf5yt5tG7Gq8RJsADOfQY8wDdTbRU3RgfiildZ98AuDdYMQKn1FkA6aZcsEdulmhm1lw9H4XU_Li8DnzEQHMx3KrKzqmvJ66K3MbQNflKoP8FI9VbUGUluIgLAnRecKlnaQmLEr_1bxSlL-GVOAAAAAVNIjQcA")
SESSION = os.environ.get("TERMUX", "AgADKFifKED3-a7xQUCzU-H-Xsu8OE-zf26yDuHLRNsxQKNCbrRixFRMGOatDi_XCgSx9nAZ-aB8LtTBbUkRru5b6WIhNLjK4peQFf1Qic7Zb36hb3ufylbi7YyBdwKV7IprqCOy0g5n6PumdetnbpIn-pnl5QuqXGF9sR5e-nWrfseX3T74RihNLmS6TnAY8S46civf5yt5tG7Gq8RJsADOfQY8wDdTbRU3RgfiildZ98AuDdYMQKn1FkA6aZcsEdulmhm1lw9H4XU_Li8DnzEQHMx3KrKzqmvJ66K3MbQNflKoP8FI9VbUGUluIgLAnRecKlnaQmLEr_1bxSlL-GVOAAAAAVNIjQcA")
token = os.environ.get("TOKEN", "5612868423:AAEhJXYpyKCV46vxjvN_0F6so05aEagBiNI")
sedthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
