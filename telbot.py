from telebot import TeleBot
from settings import config
from handlers.handler_main import HandlerMain


class TelBot:

    __version__ = config.VERSION
    __author__ = config.AUTHOR

    def __init__(self):
        self.token = config.TOKEN
        self.bot = TeleBot(self.token, threaded=False)
        self.bot.set_webhook()
        self.handler = HandlerMain(self.bot)

    def start(self):
        self.handler.handle()

    def run_bot(self):
        self.start()
        self.bot.polling(none_stop=True)


if __name__ == '__main__':
    bot = TelBot()
    bot.run_bot()

from flask import Flask, request
import telepot
import urllib3
import random

proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

secret = "234h1l234hkasdfj;kladjsfkjioq4jklj5;k"
bot = telepot.Bot('6622677042:AAHrFrwMPjsok4UzK86ByMgN3B8mAnpLqZ0')
bot.remove_webhook()
bot.setWebhook("https://halexx7.pythonanywhere.com/{}".format(secret), max_connections=1)

app = Flask(__name__)

@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    
    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        if "text" in update["message"]:
            text = update["message"]["text"]
            chat_id = update["message"]["chat"]["id"]
            if text == '/game91':
                bot.sendMessage(chat_id, "From the web: you said '{}'".format(text))


        else:
            bot.sendMessage(chat_id, "From the web: sorry, I didn't understand that kind of message")
    return "OK"


@app.route('/game91/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    update = request.get_json()

    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        if "text" in update["message"]:
            text = update["message"]["text"]
            bot.sendMessage(chat_id, "From the web: you said '{}'".format(text))
        else:
            bot.sendMessage(chat_id, "From the web: sorry, I didn't understand that kind of message")
    return "OK"


if __name__ == "__main__":
    bot.remove_webhook()
    time.sleep(1)
    bot.set_webhook(url=)


# secret = ""
# TOKEN = ''
# bot = telebot.TeleBot(TOKEN, threaded=False)
# bot.remove_webhook()
# bot.set_webhook(url="https://example.pythonanywhere.com/{}".format(secret))
