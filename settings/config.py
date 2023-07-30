import os
from emoji import emojize

TOKEN = '6622677042:AAFrK6Jq_ybW4ejOoymZLD9-vAOj72gm9kg'
NAME_DB = 'game.sqlite'
VERSION = '0.0.1'
AUTHOR = 'Aleksey Khlybov'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join('sqlite:///' + BASE_DIR, NAME_DB)

COUNT = 0

KEYBOARD = {
    'CHOOSE_GAMES': emojize(':open_file_folder: Выбрать игру'),
    'INFO': emojize(':speech_balloon: О приложении'),
    'SETTINGS': emojize('⚙️ Настройки'),

    'SEMIPRODUCT': emojize(':pizza: Полуфабрикаты'),
    'GROCERY': emojize(':bread: Бакалея'),
    'ICE_CREAM': emojize(':shaved_ice: Мороженое'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('◀️'),
    'NEXT_STEP': emojize('▶️'),
    'GAMES_91': emojize('✅ ДЕЛЕНИЕ 91'),
    'GAMES_WORD': emojize('✅ СЛОВА'),
    'X': emojize('❌'),
    'DOUWN': emojize('🔽'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'UP': emojize('🔼'),
    'APPLAY': '✅ Оформить заказ',
    'COPY': '©️'
}



COMMANDS = {
    'START': 'start',
    'HELP': 'help'
}