from settings.message import Messages
from handlers.handler import Handler
from settings import config


class HandlerAllText(Handler):

    def __init__(self, bot):
        super().__init__(bot)
        # шаг в заказе
        self.step = 0

    def pressed_btn_info(self, message):
        self.bot.send_message(message.chat.id, self.msg.welcome_msg,
                              parse_mode='HTML',
                              reply_markup=self.keyboards.info_menu())

    def pressed_btn_settings(self, message):
        self.bot.send_message(message.chat.id, self.msg.settings,
                              parse_mode='HTML',
                              reply_markup=self.keyboards.settings_menu())

    def pressed_btn_back(self, message):
        self.bot.send_message(message.chat.id, 'Вы вурнулись назад',
                               reply_markup=self.keyboards.start_menu())

    def pressed_btn_games(self, message):
        self.bot.send_message(message.chat.id, self.msg.choose_games,
                              parse_mode='HTML',
                              reply_markup=self.keyboards.choose_games())

    def pressed_btn_games_91(self, message):
        if message.text == 'exit':
            self.bot.send_message(message.chat.id, "Отличного дня!",
                                  reply_markup=self.keyboards.choose_games())
        else:
            if message.text == config.KEYBOARD['GAMES_91']:
                self.num = self.games.get_number()
                self.bot.send_message(message.chat.id, f"Сколько будет {self.num}/91 =  ")
            else:
                rslt_true = str(self.num / 91)[:8]
                if rslt_true == message.text[:8]:
                    self.bot.send_message(message.chat.id, "Отлично! Ты великолепен!")
                else:
                    self.bot.send_message(message.chat.id, f"К сожалению не верно!\nОтвет: {rslt_true}")
                self.num = self.games.get_number()
                self.bot.send_message(message.chat.id, f"Сколько будет {self.num}/91 =  ")

            self.bot.register_next_step_handler(message, self.pressed_btn_games_91)

    def pressed_btn_games_word(self, message):
        if message.text == 'exit':
            self.bot.send_message(message.chat.id, "Отличного дня!",
                                  reply_markup=self.keyboards.choose_games())
        else:
            if message.text == config.KEYBOARD['GAMES_WORD']:
                self.bot.send_message(message.chat.id, "Введите слово и ответ (Привет-веипрт): ")
            else:
                self.words = message.text.lower().split("-")
                word_sort = "".join(sorted(list(self.words[0])))
                if word_sort == self.words[1]:
                    self.bot.send_message(message.chat.id, "Отлично! Ты великолепен!")
                else:
                    self.bot.send_message(message.chat.id, f"Ответ: {word_sort}\nК сожалению не верно! Попробуй ещё раз!")
                self.bot.send_message(message.chat.id, "Введите слово и ответ (Привет-веипрт): ")
            self.bot.register_next_step_handler(message, self.pressed_btn_games_word)

    def handle(self):
        # обработчик(декоратор) сообщений,
        # который обрабатывает входящие текстовые сообщения от нажатия кнопок.
        @self.bot.message_handler(func=lambda message: True)
        def handle(message):
            # ********** меню ********** #

            if message.text == config.KEYBOARD['INFO']:
                self.pressed_btn_info(message)

            if message.text == config.KEYBOARD['SETTINGS']:
                self.pressed_btn_settings(message)

            if message.text == config.KEYBOARD['<<']:
                self.pressed_btn_back(message)

            if message.text == config.KEYBOARD['CHOOSE_GAMES']:
                self.pressed_btn_games(message)

            if message.text == config.KEYBOARD['GAMES_91']:
                self.pressed_btn_games_91(message)

            if message.text == config.KEYBOARD['GAMES_WORD']:
                self.pressed_btn_games_word(message)

