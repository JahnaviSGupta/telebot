
class TelegramBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.mode = None
        self.handlers = {}

    def add_handler(self, mode, handler):
        self.handlers[mode] = handler

    def set_mode(self, mode):
        self.mode = mode

    def process_message(self, message):
        if self.mode in self.handlers:
            handler = self.handlers[self.mode]
            handler(message)

    def start(self):
        @self.bot.message_handler(func=lambda message: True)
        def handle_message(message):
            self.process_message(message)

        self.bot.polling()