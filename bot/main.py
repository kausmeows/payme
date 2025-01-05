from bot.scheduler import schedule_reminder
from bot.logger import logger
from dotenv import load_dotenv
import asyncio
import os

# Load environment variables
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
RECIPIENTS_FILE = "data/recipients.json"
QR_FILE_PATH = "data/payment_qr.png"

async def main():
    logger.info("Starting the Telegram reminder bot...")
    logger.info("Loading recipients from %s", RECIPIENTS_FILE)
    logger.info("Using QR file: %s", QR_FILE_PATH)

    # Start reminder scheduling
    logger.info("Starting the reminder scheduler...")
    await schedule_reminder(TELEGRAM_TOKEN, RECIPIENTS_FILE, QR_FILE_PATH)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user.")
    except Exception as e:
        logger.error("An error occurred: %s", str(e))
