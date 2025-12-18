import re


class DateValidator:
    @staticmethod
    def is_valid_date(date_str: str) -> bool:
        """Проверяет формат даты ДД.ММ.ГГГГ"""
        pattern = r"^\d{2}\.\d{2}\.\d{4}$"
        return bool(re.match(pattern, date_str))


def validate_currency_code(code: str) -> bool:
    """Проверяет валидность кода валюты"""
    # Пример: USD, EUR, RUB
    return code.isalpha() and len(code) == 3


def validate_amount(amount: str) -> bool:
    """Проверяет валидность суммы"""
    try:
        float(amount)
        return True
    except ValueError:
        return False


def format_currency_response(
    amount: float, from_currency: str, to_currency: str, rate: float, result: float
) -> str:
    return f"{amount} {from_currency} = {result:.2f} {to_currency} (курс: {rate:.4f})"
