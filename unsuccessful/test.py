# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# api_token="6596543431:AAH-B6K3GBgQPKLZe8Ul3-bQoMCNz4Xsh0c"

# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello MF {update.effective_user.first_name}')

# async def whoareyou(update: Update, context: ContextTypes.DEFAULT_TYPE) ->None:
# 	await update.message.reply_text(f'I am going to be your new bot nigga')

# app = ApplicationBuilder().token(api_token).build()

# app.add_handler(CommandHandler("hello", hello))
# app.add_handler(CommandHandler("whoareyou",whoareyou))

# app.run_polling()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import threading, time, re

api_token="6596543431:AAH-B6K3GBgQPKLZe8Ul3-bQoMCNz4Xsh0c"

class Command: 
	
	async def whoareyou(self,update: Update, context: ContextTypes.DEFAULT_TYPE) ->None:
		await update.message.reply_text(f'I am going to be your new bot nigga')

	async def hello(self,update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	    await update.message.reply_text(f"Hello pedis {update.effective_user.first_name}")
		
	async def mydescription(self,update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
		if update.effective_user.first_name == "R":
			await update.message.reply_text(f"hello")

	async def echo(self,update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
		await context.bot.send_message(chat_id=update.effective_chat.id, text=context.args[0])

	async def imagine(self,update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
		print(update.effective_user)

		param=' '.join(context.args)
		print(param)

	async def echos(self,update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
		text=update.message.text
		print("running")
		print(text)

chat_ids=[]
async def send(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
	if update.message.text.lower()=="who are you":
		chat_ids.append(update.message.chat_id)
		print(chat_ids)

		print(update.effective_user)

		for chat_id in chat_ids:
			sent_message=await context.bot.send_message(chat_id=chat_id,text="any assistance")
			print("sending message",chat_id)
			print("updating message")
			print(sent_message)
			for i in range(3):
				# updating 
				await context.bot.edit_message_text(chat_id=chat_id,message_id=sent_message.message_id,text=str(i))
				time.sleep(3)
		print(chat_ids,update.message.text)

async def rishabh(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
		print("called rishabh")
		pattern1=r"\bjesus\b"
		pattern2=r"\babusing\b"
		pattern3=r"\bplay\b"
		text=update.message.text
		if re.findall(pattern1,text,re.IGNORECASE):
			# await context.bot.send_message(chat_id=update.message.chat_id,text="EMERGENCY FOUND\n Calling hamshini father")
			await context.bot.send_photo(chat_id=update.message.chat_id,photo=open("download.jpg",'rb'))
		print("half",text)
		if re.findall(pattern2,text,re.IGNORECASE):
			print("sdfdsf")
			await context.bot.send_message(chat_id=update.message.chat_id,text="EMERGENCY FOUND\n Calling hamshini father")
		if re.findall(pattern3,text,re.IGNORECASE):
			data="this is pushpaltha speaking rishaba meet me immidiately"
			message=await context.bot.send_message(chat_id=update.message.chat_id,text="releasing the danger")
			print(message)
			test=""
			for elements in data.split():
				time.sleep(0.5)
				test+=elements+" "
				await context.bot.edit_message_text(chat_id=update.message.chat_id,message_id=message.message_id,text=test)
c=Command()

app = ApplicationBuilder().token(api_token).build()

app.add_handler(CommandHandler("hello", c.hello))
app.add_handler(CommandHandler("whoareyou",c.whoareyou))
app.add_handler(CommandHandler("mydescription",c.mydescription))
app.add_handler(CommandHandler("echo",c.echo))
app.add_handler(CommandHandler("imagine",c.imagine))


# message_handler = MessageHandler(filters.ALL, c.echos)
# app.add_handler(message_handler)


# app.add_handler(MessageHandler(filters.TEXT,send))

app.add_handler(MessageHandler(filters.TEXT,rishabh))


app.run_polling()



