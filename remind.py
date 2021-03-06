import telebot

from telebot import types

import time

import threading

import logging

bot = telebot.TeleBot("400097540:AAF6iHaEHszGa7imNitGqdewGRdsWNOtJoM")

reminder = ""

def time_loop(chat_id, minutes, reminder):
	seconds = int(minutes) * 60
	while(seconds > 0):
		seconds = seconds - 1
		time.sleep(1)
	bot.send_message(chat_id, "!!!\t\t"+reminder+"\t\t!!!")
	mins = ""
	reminder = ""

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
	bot.reply_to(message, "Hi I'm RemindAllBot, I'll send you reminders! Type /remind to get started!")

@bot.message_handler(commands=['remind'])
def start_remind_queries(message):
	markup = types.ForceReply(selective=False)
	msg = bot.reply_to(message,"What would you like the reminder to say?",reply_markup=markup)
	bot.register_next_step_handler(msg, process_reminder_step)

def process_reminder_step(message):
	try:
		global reminder
		chat_id = str (message.chat.id)
		reminder = message.text
		markup = types.ForceReply(selective=False)
		msg = bot.reply_to(message,"In how many minutes would you like to be reminded?", reply_markup = markup)
		bot.register_next_step_handler(msg, process_mins_step)
	except Exception as e:
		print(e)
		bot.reply_to(message, "i goofed, try again")

def process_mins_step(message):
	try:
		global reminder
		mins = message.text
		bot.send_message(message.chat.id, "Great! I'll remind you to " + reminder + " in " + mins + " minutes!")
		t1=threading.Thread(target=time_loop, args=(message.chat.id, mins, reminder))
		t1.start()
		reminder = ""
	except Exception as e:
		print(e)
		bot.reply_to(message, "i goofed, try again")

bot.polling()