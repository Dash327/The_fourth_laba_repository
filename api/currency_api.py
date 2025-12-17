import requests
import json
from datetime import datetime
from typing import Dict, Optional
from utils.exceptions import APIError
from config import Config


class CurrencyAPI:
    def __init__(self):
        self.base_url = Config.CBR_CURRENT_URL
        self.archive_url = Config.CBR_ARCHIVE_URL

    def get_current_rates(self) -> Dict:
        """Получение текущих курсов валют"""
        try:
            response = requests.get(self.base_url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise APIError(f"Ошибка соединения: {e}")
        except json.JSONDecodeError as e:
            raise APIError(f"Ошибка парсинга JSON: {e}")

    def get_historical_rates(self, date_str: str) -> Dict:
        try:
            day, month, year = date_str.split(".")

            url = self.archive_url.format(year=year, month=month, day=day)

            # Запрос
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            return response.json()

        except ValueError:
            raise APIError("Неверный формат даты")
        except requests.RequestException as e:
            if response.status_code == 404:
                raise APIError("Данные за эту дату не найдены")
            raise APIError(f"Ошибка API: {e}")

    def get_specific_currency(
        self, currency_code: str, date: Optional[str] = None
    ) -> float:
        """Получение курса конкретной валюты"""
        if date:
            data = self.get_historical_rates(date)
        else:
            data = self.get_current_rates()

        if currency_code in data.get("Valute", {}):
            return data["Valute"][currency_code]["Value"]
        else:
            raise APIError(f"Валюта {currency_code} не найдена")
