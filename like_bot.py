import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackContext
from telegram import Update
from handler import start
import logging

import os

# get token from environment variable
TOKEN = os.environ['TOKEN'] 

# Updater 
updater = Updater(token=TOKEN)

# Dispatcher
dp = updater.dispatcher



dp.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()

