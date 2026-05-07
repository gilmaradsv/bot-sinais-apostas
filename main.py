from telegram.ext import Application
import asyncio
from handlers.signals import receive_signal
from handlers.callbacks import button_callback
from handlers.dashboard import dashboard
from config import TOKEN

async def main():
    app = Application.builder().token(TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("dashboard", dashboard))
    app.add_handler(MessageHandler(filters.TEXT & \~filters.COMMAND, receive_signal))
    app.add_handler(CallbackQueryHandler(button_callback))

    print("🤖 Bot iniciado...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
