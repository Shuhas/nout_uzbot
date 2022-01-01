from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters

from Service import *

try:
    create_table()
    insert_into()
except Exception as e:
    pass
