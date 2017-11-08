import telebot

bot = telebot.TeleBot("400097540:AAF6iHaEHszGa7imNitGqdewGRdsWNOtJoM")

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
	bot.reply_to(message, "Hi I'm RemindAllBot, I'll send you reminders! Type /remind to get started!")

bot.polling()