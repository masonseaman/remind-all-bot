import telebot

from telebot import types

bot = telebot.TeleBot("400097540:AAF6iHaEHszGa7imNitGqdewGRdsWNOtJoM")

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
	bot.reply_to(message, "Hi I'm RemindAllBot,x I'll send you reminders! Type /remind to get started!")

@bot.message_handler(commands=['remind'])
def start_remind_queries(message):
	markup = types.ForceReply(selective=False)
	bot.reply_to(message,"In how many minutes would you like to be reminded?",reply_markup=markup)
	mins = message.text
	bot.send_message(chatid,int(mins))
	
bot.polling()