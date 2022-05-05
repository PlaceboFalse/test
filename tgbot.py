import telebot
from telebot import types

s = open('bots.txt')
print(s.read())

bot = telebot.TeleBot("")


@bot.message_handler(commands=['start', 'help'])
def send_start(message):
	if message.text == '/start':

		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton("Первая кнопка")
		item2 = types.KeyboardButton("Вторая кнопка")
		markup.add(item1, item2)
		# 2 большие кнопки

		# bot.send_message(message.chat.id,'список пуст', reply_markup = markup)

	else:
		markup = types.InlineKeyboardMarkup(row_width=2)
		item1 = types.InlineKeyboardButton("Бесплатно", callback_data='first')
		item2 = types.InlineKeyboardButton("Платно", callback_data='second')
		markup.add(item1, item2)
		# 2 под сообщением бота


@bot.message_handler(content_types=['text'])
def send_text(message):
	# for всех мест в зависимости от кнопок на старте

	bot.send_message(message.chat.id, "Описание места")
	x = 43.9783
	y = 15.3830
	bot.send_location(message.chat.id, x, y)


bot.polling(none_stop=True)


# сортировки.
# Спорт комплексы