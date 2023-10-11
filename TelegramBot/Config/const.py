import configparser
from pathlib import Path
import sys

config = configparser.ConfigParser()
PATH = Path(__file__).resolve().parent
config.read(str(PATH) + '/config.ini')

BOT_TOKEN = config["Telegram"]["bot_token"]