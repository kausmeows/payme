import asyncio
from telegram import Bot
from bot.utils import load_recipients
from bot.logger import logger

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


async def schedule_reminder(bot_token, recipients_file, qr_file_path):
    """
    Immediately send a reminder and then keep sending it every 5 seconds.
    """
    while True:
        logger.info("Running scheduled reminder...")
        await send_reminder(bot_token, recipients_file, qr_file_path)
        logger.info("Reminder sent. Waiting for the next cycle...")
        # Wait for 5 seconds before sending the next reminder
        await asyncio.sleep(5)
