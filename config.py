import os
from dotenv import load_dotenv

load_dotenv()  # Загружает переменные из .env файла


class Config:

    TELEGRAM_TOKEN = os.getenv(
        "TELEGRAM_TOKEN", "8209594012:AAGMKWV-OrBMJ4ZbPAin5UevmEHNnDz9q7I"
    )

    # API URLs
    CBR_CURRENT_URL = "https://www.cbr-xml-daily.ru/daily_json.js"
    CBR_ARCHIVE_URL = (
        "https://www.cbr-xml-daily.ru/archive/{year}/{month}/{day}/daily_json.js"
    )

    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///bot_database.db")

    DATA_DIR = "data/"
    LOG_FILE = "bot.log"

    DEFAULT_CURRENCIES = ["USD", "EUR", "CNY", "GBP"]

    MAX_HISTORY_DAYS = 365 * 5  # 5 лет максимум
