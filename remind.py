import telebot

from telebot import types

import time

import threading

bot = telebot.TeleBot("400097540:AAF6iHaEHszGa7imNitGqdewGRdsWNOtJoM")

chat_id = ""

mins = ""
reminder = ""

def time_loop(minutes):
	global mins, reminder
	seconds = minutes * 60
	while(seconds > 0):
		seconds = seconds - 1
		sleep(1)
	bot.send_message(chat_id, "!!!\t\t"+reminder+"\t\t!!!")
	mins = ""
	reminder = ""

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
	bot.reply_to(message, "Hi I'm RemindAllBot,x I'll send you reminders! Type /remind to get started!")

@bot.message_handler(commands=['remind'])
def start_remind_queries(message):
	markup = types.ForceReply(selective=False)
	msg = bot.reply_to(message,"In how many minutes would you like to be reminded?",reply_markup=markup)
	bot.register_next_step_handler(msg, process_mins_step)

def process_mins_step(message):
	try:
		global mins
		global chat_id
		chat_id = message.chat.id
		mins = message.text
		markup = types.ForceReply(selective=False)
		msg = bot.reply_to(message,"What would you like the reminder to say?", reply_markup = markup)
		bot.register_next_step_handler(msg, process_reminder_step)
	except Exception as e:
		bot.reply_to(message, 'oooops')

def process_reminder_step(message):
	try:
		global reminder, mins
		chat_id = message.chat.id
		reminder = message.text
		bot.send_message(chat_id, "Great! I'll remind you to " + reminder + " in " + mins + " minutes!")
		t1=threading.Thread(target=time_loop, mins)
	except Exception as e:
		bot.reply_to(message, 'oooops')

bot.polling()