# Telegram libraries
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# External libraries
from exlibs import dictionary

# Common
import common

#general libraries


class Command:
    # /command
    # async def __init__(self):
    #     self.shell_object=None #If shell created
    #     self.current_shell_user=None
        

    async def help(self,update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
        await update.message.reply_text("List of available command are\n"
                                        "/help - Lists all available commands\n"
                                        "/hello - Says Hello there\n"
                                        "/meaning - Gives meaning of words\n")
    async def hello(self,update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
        await update.message.reply_text(f"Hello there {update.effective_user.first_name}") 
    
    async def meaning(self,update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
        meanf=dictionary.Dictionary()
        # args=" ".join(update.message.text)
        args=" ".join(context.args)
        data= meanf.meaning(args)
        if not data:
            data="Sorry nothing found\n"
        await update.message.reply_text(data)
    
    # async def activate_shell(self, update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
    #     self.current_shell_user=update.effective_user #making sure only current user uses 
    #     self.shell_object=shell.Shell()    #Begins shell 
    #     #(Optional) Add additional security features to prevent misuse

    # async def run_command(self,update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
    #     pass
            
    async def shell(self,update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
        common.shell_userid=update.effective_user #Effective user
        common.shell_message_flag=True  #Setting shell flag active
        await update.message.reply_text("Shell started\n Use terminate_shell to terminate")
        print("Shell started")

    
    async def ytd(self,update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
        await context.bot.send_video(chat_id=update.message.chat_id,video=open("./tempDownloads/YouTube Rewind 2019 For the Record  YouTubeRewind.mp4",'rb'),connect_timeout=60)
        

    
        




    