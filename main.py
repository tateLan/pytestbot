
import telebot
import insta_handler
import instaloader

bot = telebot.TeleBot('816025427:AAHFPoMUuK6Izxy4OtGcoSGKxCWXTgbF-Xw')

inst_handlr = insta_handler.Insta_handler()

@bot.message_handler(commands=['start', 'relogin'])
def start(message):
  sent = bot.send_message(message.chat.id, 'enter yr insta login, bruh')
  bot.register_next_step_handler(sent, enter_login)

def enter_login(message):
    inst_handlr.login = message.text

    sent = bot.send_message(message.chat.id, 'and pass pls')
    bot.register_next_step_handler(sent, enter_pass)

def enter_pass(message):
        inst_handlr.password = message.text

        if(try_login()):
            loader = inst_handlr.init_loader()
            inst_handlr.init_profile(loader)

            bot.delete_message(message.chat.id, message_id=message.message_id)
            bot.send_message(message.chat.id, 'mssg with pass deleted for security :)')

def try_login():
    try:
        loader = inst_handlr.init_loader()
        return True
    except:
        return False

# @bot.message_handler(content_types=['text'])
# def send_text(message):
#     if message.text.lower() == 'followers':
#         bot.send_message(message.chat.id, 'Привет, мой создатель')
#     elif message.text.lower() == 'пока':
#         bot.send_message(message.chat.id, 'Прощай, создатель')

bot.polling()
