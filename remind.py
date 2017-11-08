
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

#help command
def help(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Welcome to reminder bot, I can send you reminders. Try /remind")
		
help_handler = CommandHandler('help', help)

#remind command
def remind(bot, update):
	

def main():
	updater = Updater(token="400097540:AAF6iHaEHszGa7imNitGqdewGRdsWNOtJoM")
	dispatcher = updater.dispatcher


	#enable commands
	dispatcher.add_handler(help_handler)
	dispatcher.add_handler(CallbackQueryHandler(button))
	dispatcher.add_handler(CommandHandler('remind',remind))

	#enable messages

	updater.start_polling()

	updater.idle()

if __name__ == '__main__':
	main()

