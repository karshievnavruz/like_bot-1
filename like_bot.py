import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackContext
from telegram import Update
from handler import start, get_image
import logging

import os

# get token from environment variable
TOKEN = os.environ['TOKEN'] 

# Updater 
updater = Updater(token=TOKEN)

# Dispatcher
dp = updater.dispatcher



dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.photo, get_image))
updater.start_polling()
updater.idle()

