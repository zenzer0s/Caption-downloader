import logging
import instaloader
import nest_asyncio
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# Apply nest_asyncio patch to allow nested event loops.
nest_asyncio.apply()

# Initialize Instaloader (for Instagram scraping)
loader = instaloader.Instaloader()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

BOT_TOKEN = "8185026608:AAEvJmLNJuijF8R4_F23JOcZRvyf8K-JIcA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Send me an Instagram Reel link, and I'll fetch the caption!")

async def get_caption(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_text = update.message.text
    if "instagram.com/reel/" in message_text:
        try:
            shortcode = message_text.split("/")[-2]
            post = instaloader.Post.from_shortcode(loader.context, shortcode)
            caption = post.caption if post.caption else "No caption found."
            await update.message.reply_text(f"Caption:\n{caption}")
        except Exception as e:
            await update.message.reply_text("Failed to fetch caption. Ensure the link is correct and the post is public.")
    else:
        await update.message.reply_text("Please send a valid Instagram Reel link.")

async def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_caption))
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
