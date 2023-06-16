# import telebot
from telegrambot import TelegramBot

def mode1_handler(message):
    # Logic for handling messages in mode 1
    print("Mode 1:", message.text)

def mode2_handler(message):
    # Logic for handling messages in mode 2
    print("Mode 2:", message.text)

# Create an instance of TelegramBot
bot = TelegramBot("YOUR_TELEGRAM_BOT_TOKEN")

# Add handlers for different modes
bot.add_handler("mode1", mode1_handler)
bot.add_handler("mode2", mode2_handler)

# Set the initial mode
bot.set_mode("mode1")

# Start the bot
bot.start()