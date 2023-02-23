import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackContext
from telegram import Update
import logging

import os

# get token from environment variable
TOKEN = os.environ['TOKEN'] 

# Updater 
updater = Updater(token=TOKEN)

# Dispatcher
dp = updater.dispatcher

# Handler for /start command
def start(update:Update, context:CallbackContext):
    update.message.reply_text('Hi!')


dp.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()

