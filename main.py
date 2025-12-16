import logging
from bot.bot import CurrencyBot
from config import Config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(Config.LOG_FILE), logging.StreamHandler()],
)

logger = logging.getLogger(__name__)


def main():
    try:
        logger.info("Запуск бота...")

        bot = CurrencyBot(Config.TELEGRAM_TOKEN)

        # Запускаем бота
        bot.run()

    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}")
        raise


if __name__ == "__main__":
    main()
