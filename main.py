import telebot

bot = telebot.TeleBot("1176060471:AAFzSpKbr0c8_3drV99T8jhU00EHMV6IB9Q")


@bot.message_handler(content_types=['text'])
def start(message):
    bot.send_message(message.chat.id, "Hello")


bot.polling()
