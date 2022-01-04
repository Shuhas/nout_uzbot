from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters

from Service import *

try:
    create_table()
    insert_into()
except Exception as e:
    pass


def start(update, context):
    user = update.message.from_user
    if get_one(user.id):
        pass
    else:
        create_user(user_id=user.id, username=user.username)
    update.message.reply_text("Assalomu alaykum ismingizni kiriting")

def recieved_message(update, context):
    pass


def main():
    TOKEN = "5060155479:AAGjHg8InuzHNDHrJnEeq8rr7x32QSA09DM"
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
