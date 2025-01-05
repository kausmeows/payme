from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from telegram import Bot
from bot.utils import load_recipients
from bot.logger import logger
import asyncio

async def send_reminder(bot_token, recipients_file, qr_file_path):
    """
    Send the reminder message with the attached QR code to all recipients asynchronously.
    """
    bot = Bot(bot_token)
    chat_ids = load_recipients(recipients_file)
    message = "Reminder: Please pay @kaus_mos for the YouTube Family Subscription."

    for chat_id in chat_ids:
        try:
            logger.info("Sending message to chat_id: %s", chat_id)
            await bot.send_message(chat_id, message)
            with open(qr_file_path, "rb") as qr_file:
                await bot.send_photo(chat_id, photo=qr_file)
            logger.info("Message sent successfully to chat_id: %s", chat_id)
        except Exception as e:
            logger.error(
                "Failed to send message to chat_id %s: %s", chat_id, e)


async def start_scheduler(bot_token, recipients_file, qr_file_path):
    """
    Start the scheduler to send reminders on the 23rd of every month at 9 AM.
    """
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        send_reminder,
        CronTrigger(day=23, hour=9, minute=0),
        args=[bot_token, recipients_file, qr_file_path],
        id="monthly_reminder",
    )
    scheduler.start()
    logger.info("Scheduler started. Reminder will run on the 23rd of every month at 9 AM.")

    # Keep the scheduler running
    while True:
        await asyncio.sleep(1)
