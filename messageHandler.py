from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
#common file
import common

#External libs
from exlibs import shell


class Messages:
    def __init__(self):
        self.sh=None

    async def handle_text(self,update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
        if common.shell_message_flag:
            self.sh=shell.Shell()
            print("handling shell command")
            
            if(update.effective_user==common.shell_userid):
                self.command=update.message.text #user command
                command=self.command
                if command.lower()=="terminate_shell": #shell termination
                    self.sh=None
                    common.shell_message_flag=False
                    common.shell_userid=None
                    await context.bot.send_message(chat_id=update.message.chat_id,text="Terminated shell") 
                    print("terminated shell") 
                    return
                await context.bot.send_message(chat_id=update.message.chat_id,text=self.sh.run_command(self.command))  #run command and send user message
                
            
                

        