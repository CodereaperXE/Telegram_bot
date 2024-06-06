# Telegram libraries
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
#general libraries
import json
#user defined commands library
import commands
import messageHandler
#common file
import common


#from dotenv import load_dotenv
#import os
#load_dotenv()
#api_token=os.getenv('api_token')


# Application section
api_token=None
with open("config.json",'r') as file:
    config=json.load(file)
    api_token=config["api_token"]




app = ApplicationBuilder().token(api_token).build()

# Command handler section

#Instance section
coms=commands.Command()
mes=messageHandler.Messages()
common_in=common #Common

#Command handler section
app.add_handler(CommandHandler("help",coms.help))
app.add_handler(CommandHandler("hello",coms.hello))
app.add_handler(CommandHandler("meaning",coms.meaning))
app.add_handler(CommandHandler("shell",coms.shell))
app.add_handler(CommandHandler("ytd",coms.ytd))
#Message handler section
app.add_handler(MessageHandler(filters.TEXT,mes.handle_text))


# Polling
app.run_polling()


