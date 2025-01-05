import asyncio
from bot.scheduler import start_scheduler
from bot.logger import logger
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
RECIPIENTS_FILE = "data/receivers.json"
QR_FILE_PATH = "data/payment_qr.png"

async def main():
    logger.info("Starting the Telegram reminder bot...")
    logger.info("Using recipients file: %s", RECIPIENTS_FILE)
    logger.info("Using QR file: %s", QR_FILE_PATH)

    # Start the scheduler
    await start_scheduler(TELEGRAM_TOKEN, RECIPIENTS_FILE, QR_FILE_PATH)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user.")
    except Exception as e:
        logger.error("An error occurred: %s", str(e))
