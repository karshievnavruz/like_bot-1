import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackContext
from telegram import Update
import logging
import requests
# Handler for /start command
def start(update:Update, context:CallbackContext):

    update.message.reply_text('Hi!')

# Handler for get image
def get_image(update:Update, context:CallbackContext):
    """
    Get the image from the user and send to backend
    """
    # Get the message id
    message_id = update.message.message_id
    # Get image id
    image_id = update.message.photo[-1].file_id
    # Print message id and image id to the log

    print(f"Message id: {message_id}, Image id: {image_id}")
    # Send image to backend
    # endpoint url
    url = 'http://motof.pythonanywhere.com/api/addImage'
    # Payload
    payload = {
        'message_id': message_id,
        'image_id': image_id
    }
    # Send request
    response = requests.post(url, json=payload)
    # Print status code
    print(response.status_code)
    update.message.reply_text('Got image')