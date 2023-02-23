import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackContext
from telegram import Update

# Handler for /start command
def start(update:Update, context:CallbackContext):
    update.message.reply_text('Hi!')
