from flask import Flask, request
import telebot
import random
from telebot.types import KeyboardButton, ReplyKeyboardMarkup

secret = "234h1l234hkasdfj;kladjsfkjioq4jklj5;k"
bot = telebot.TeleBot('6622677042:AAHrFrwMPjsok4UzK86ByMgN3B8mAnpLqZ0', threaded=False)

bot.remove_webhook()
bot.set_webhook(url="https://halexx7.pythonanywhere.com/{}".format(secret))


app = Flask(__name__)
@app.route('/{}'.format(secret), methods=["POST"])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


def start_command(message):
    bot.send_message(message.chat.id, 'Hi *' + message.chat.first_name + '*!' ,
    parse_mode='Markdown',
    reply_markup=start_menu())


num = None
nums = range(11, 90)
def games_91(message):
    global num
    if message.text == 'exit':
        bot.send_message(message.chat.id, "Отличного дня!",
                         reply_markup=start_menu())
    else:
        if message.text == 'game_91':
            num = random.choice(nums)
            bot.send_message(message.chat.id,
                             f"Сколько будет *{num}/91* =  ",
                             parse_mode='Markdown',
                             reply_markup=exit_game())
        else:
            rslt_true = str(num / 91)[:8]
            if rslt_true == message.text[:8]:
                bot.send_message(message.chat.id,
                                 "Отлично! Ты великолепен!")
            else:
                bot.send_message(message.chat.id,
                                 f"К сожалению не верно!\nОтвет: *{rslt_true}*",
                                 parse_mode='Markdown')
                print('Отдали сообщение')
            num = random.choice(nums)
            bot.send_message(message.chat.id,
                             f"Сколько будет *{num}/91* =  ",
                             parse_mode='Markdown',
                             reply_markup=exit_game())

        bot.register_next_step_handler(message, games_91)

def game_word(message):
    if message.text == 'exit':
        bot.send_message(message.chat.id, "Отличного дня!",
                         reply_markup=start_menu())
    else:
        if message.text == 'game_word':
            bot.send_message(message.chat.id,
                            "Введите слово и ответ через пробел\nПример: *Привет веипрт*: ",
                            parse_mode='Markdown',
                            reply_markup=exit_game())
        else:
            words = message.text.lower().split(" ")
            word_sort = "".join(sorted(list(words[0])))
            if word_sort == words[1]:
                bot.send_message(message.chat.id, "Отлично! Ты великолепен!")
            else:
                bot.send_message(message.chat.id,
                                 f"Ответ: *{word_sort}*\nК сожалению не верно! Попробуй ещё раз!",
                                 parse_mode='Markdown')
            bot.send_message(message.chat.id,
                            "Введите слово и ответ через пробел\nПример: *Привет веипрт*: ",
                            parse_mode='Markdown',
                            reply_markup=exit_game())
        bot.register_next_step_handler(message, game_word)

@bot.message_handler(func=lambda message: True)
def handle(message):
    # ********** меню ********** #

    if message.text == "game_91":
        games_91(message)
    if message.text == "game_word":
        game_word(message)
    if message.text == "start":
        start_command(message)


def set_btn(name, step=0, quantity=0):
    return KeyboardButton(name)

def start_menu():
    markup = ReplyKeyboardMarkup(True, True)
    itm_btn_1 = set_btn('start')
    itm_btn_2 = set_btn('game_91')
    itm_btn_3 = set_btn('game_word')
    # расположение кнопок в меню
    markup.row(itm_btn_1)
    markup.row(itm_btn_2, itm_btn_3)
    return markup

def exit_game():
    markup = ReplyKeyboardMarkup(True, True)
    itm_btn_1 = set_btn('exit')
    # расположение кнопок в меню
    markup.row(itm_btn_1)
    return markup

