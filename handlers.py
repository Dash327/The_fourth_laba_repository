import logging
from api.currency_api import CurrencyAPI
from database.repository import UserRepository
from utils.validators import DateValidator
from utils.formatters import format_currency_response
from utils.exceptions import APIError, ValidationError

logger = logging.getLogger(__name__)


class MessageHandlers:
    def __init__(self, bot):
        self.bot = bot
        self.api = CurrencyAPI()
        self.user_repo = UserRepository()
        self.validator = DateValidator()

    def handle_start(self, message):
        try:
            welcome_text = (
                "Добрый день! Я бот для отслеживания курсов валют.\n\n"
                "Доступные команды:\n"
                "/rate - текущий курс\n"
                "/archive - курс на дату\n"
                "/convert - конвертер\n"
                "/settings - настройки\n"
                "/favorites - избранные валюты\n"
                "/help - помощь\n\n"
                "Примеры:\n"
                "Просто отправьте '100 USD to RUB' для конвертации"
            )
            self.bot.send_message(message.chat.id, welcome_text)

            # Сохраняем пользователя в БД
            self.user_repo.create_user_if_not_exists(
                user_id=message.from_user.id,
                username=message.from_user.username,
                first_name=message.from_user.first_name,
            )

        except Exception as e:
            logger.error(f"Ошибка в handle_start: {e}")
            self.bot.send_message(
                message.chat.id, "⚠️ Произошла ошибка. Попробуйте позже."
            )

    def handle_rate(self, message):
        try:
            rates = self.api.get_current_rates()
            response_text = format_currency_response(rates)
            self.bot.send_message(message.chat.id, response_text, parse_mode="HTML")

        except APIError as e:
            self.bot.send_message(message.chat.id, f"❌ Ошибка API: {e}")
        except Exception as e:
            logger.error(f"Ошибка в handle_rate: {e}")
            self.bot.send_message(message.chat.id, "⚠️ Не удалось получить курсы валют")

    def handle_archive(self, message):
        try:
            self.bot.send_message(
                message.chat.id,
                "📅 Введите дату в формате ДД.ММ.ГГГГ (например, 15.12.2023):",
            )
            self.bot.register_next_step_handler(message, self._process_archive_date)

        except Exception as e:
            logger.error(f"Ошибка в handle_archive: {e}")

    def _process_archive_date(self, message):
        try:
            date_str = message.text.strip()

            if not self.validator.is_valid_date(date_str):
                raise ValidationError("Неверный формат даты. Используйте ДД.ММ.ГГГГ")

            # Получение курса на дату
            rates = self.api.get_historical_rates(date_str)
            response_text = format_currency_response(rates, date_str)

            self.bot.send_message(message.chat.id, response_text, parse_mode="HTML")

        except ValidationError as e:
            self.bot.send_message(message.chat.id, f"{e}")
        except APIError as e:
            self.bot.send_message(message.chat.id, f"Ошибка API: {e}")
        except Exception as e:
            logger.error(f"Ошибка в _process_archive_date: {e}")
            self.bot.send_message(message.chat.id, "Не удалось получить данные")
