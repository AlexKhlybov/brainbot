from settings import config
from games.games import Games
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
from data_base.dbalchemy import DBManager


class Keyboards:
    """
    Класс Keyboards предназначен для создания и разметки интерфейса бота
    """
    # Инициализация разметки

    def __init__(self):
        self.markup = None
        # self.BD = DBManager()
        self.games = Games()

    def set_btn(self, name, step=0, quantity=0):
        """
        Создает и возвращает кнопку по входным параметрам
        """
        return KeyboardButton(config.KEYBOARD[name])

    def start_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('CHOOSE_GAMES')
        itm_btn_2 = self.set_btn('INFO')
        itm_btn_3 = self.set_btn('SETTINGS')
        # расположение кнопок в меню
        self.markup.row(itm_btn_1)
        self.markup.row(itm_btn_2, itm_btn_3)
        return self.markup

    def info_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')
        # расположение кнопок в меню
        self.markup.row(itm_btn_1)
        return self.markup

    def settings_menu(self):
        """
        Создает разметку кнопок в меню 'Настройки'
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1)
        return self.markup

    def choose_games(self):
        """
        Создает разметку кнопок в меню 'Настройки'
        """
        self.markup = ReplyKeyboardMarkup(True, True)

        itm_btn_1 = self.set_btn('GAMES_91')
        itm_btn_2 = self.set_btn('GAMES_WORD')
        itm_btn_3 = self.set_btn('<<')
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1, itm_btn_2)
        self.markup.row(itm_btn_3)
        return self.markup

    def get_games_91(self):
        """
        Создает разметку кнопок в меню 'Настройки'
        """
        self.markup = ReplyKeyboardMarkup(True, True)

        itm_btn_1 = self.set_btn('GAMES_91')
        itm_btn_2 = self.set_btn('GAMES_WORD')
        itm_btn_3 = self.set_btn('<<')
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1, itm_btn_2)
        self.markup.row(itm_btn_3)
        return self.markup
