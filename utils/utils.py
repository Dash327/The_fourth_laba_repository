import re


class DateValidator:
    @staticmethod
    def is_valid_date(date_str: str) -> bool:
        """Проверяет формат даты ДД.ММ.ГГГГ"""
        pattern = r"^\d{2}\.\d{2}\.\d{4}$"
        return bool(re.match(pattern, date_str))
