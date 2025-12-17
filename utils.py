import re
from datetime import datetime
from utils.exceptions import ValidationError


class DateValidator:
    @staticmethod
    def is_valid_date(date_str: str) -> bool:
        pattern = r"^\d{2}\.\d{2}\.\d{4}$"
        if not re.match(pattern, date_str):
            return False

        try:
            day, month, year = map(int, date_str.split("."))
            datetime(year, month, day)
            return True
        except ValueError:
            return False

    @staticmethod
    def validate_currency_code(code: str) -> bool:
        return bool(re.match(r"^[A-Z]{3}$", code))


class InputValidator:
    @staticmethod
    def validate_conversion_input(text: str) -> tuple:
        pattern = r"^(\d+(?:\.\d+)?)\s+([A-Z]{3})\s+to\s+([A-Z]{3})$"
        match = re.match(pattern, text.strip(), re.IGNORECASE)

        if not match:
            raise ValidationError("Неверный формат. Используйте: '100 USD to RUB'")

        amount = float(match.group(1))
        from_currency = match.group(2).upper()
        to_currency = match.group(3).upper()

        return amount, from_currency, to_currency
