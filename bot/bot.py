import telebot
from telebot import types
from bot.keybords import get_main_keyboard
import logging
from .handlers import MessageHandlers
from config import Config
from bot.keybords import Keyboards

logger = logging.getLogger(__name__)


class CurrencyBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.handlers = MessageHandlers(self.bot)
        self.keyboards = Keyboards()
        self.setup_handlers()

    def setup_handlers(self):
        # Команды
        self.bot.message_handler(commands=["start"])(self.handlers.handle_start)
        self.bot.message_handler(commands=["help"])(self.handlers.handle_help)
        self.bot.message_handler(commands=["rate"])(self.handlers.handle_rate)
        self.bot.message_handler(commands=["archive"])(self.handlers.handle_archive)
        self.bot.message_handler(commands=["settings"])(self.handlers.handle_settings)
        self.bot.message_handler(commands=["favorites"])(self.handlers.handle_favorites)

        self.bot.callback_query_handler(func=lambda call: True)(
            self.handlers.handle_callback
        )

        self.bot.message_handler(func=lambda msg: True)(
            self.handlers.handle_any_message
        )

    def run(self):
        logger.info("Бот запущен и ожидает сообщений...")
        self.bot.polling(none_stop=True, interval=0)
