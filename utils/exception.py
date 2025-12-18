class APIError(Exception):
    """Ошибка при работе с API"""

    pass


class ValidationError(Exception):
    """Ошибка валидации данных"""

    pass
