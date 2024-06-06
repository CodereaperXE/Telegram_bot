from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ApplicationBuilder

# Define a function to start the bot
async def start(update, context):
    # Create a list of button(s)
    keyboard = [
        [InlineKeyboardButton("Option 1", callback_data='1')],
        [InlineKeyboardButton("Option 2", callback_data='2')]
    ]
    # Create a markup with the defined buttons
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send a message with the buttons
    await update.message.reply_text('Please choose:', reply_markup=reply_markup)

# Define a function to handle button clicks
async def button(update, context):
    query = update.callback_query
    # Send a message based on which button was clicked
    if query.data == '1':
        await query.edit_message_text(text="You've chosen Option 1")
    elif query.data == '2':
        await query.edit_message_text(text="You've chosen Option 2")

# Create an Updater and pass in your bot's token
api="6596543431:AAH-B6K3GBgQPKLZe8Ul3-bQoMCNz4Xsh0c"
dp= ApplicationBuilder().token(api).build()


# Get the dispatcher to register handlers

# Add command handler to start the bot
dp.add_handler(CommandHandler("start", start))

# Add callback query handler to handle button clicks
dp.add_handler(CallbackQueryHandler(button))

# Start the 
dp.run_polling()

