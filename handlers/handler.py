import abc
from games.games import Games
from settings.message import Messages
from markup.markup import Keyboards
from data_base.dbalchemy import DBManager

class Handler(metaclass=abc.ABCMeta):

    def __init__(self, bot):
        # получаем объект бота
        self.bot = bot
        self.games = Games()
        self.msg = Messages()
        # инициализируем разметку кнопок
        self.keyboards = Keyboards()
        self.DB = DBManager()

    @abc.abstractmethod
    def handle(self):
        pass

