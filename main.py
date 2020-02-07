import os
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler


def cs_callback(bot, update: Update, **optional_args):
    update.message.reply_text("CS CS CS?", quote=False)
    update.message.reply_text("C", quote=False)
    update.message.reply_text("S", quote=False)
    update.message.reply_text("?", quote=False)
    update.message.reply_text(os.environ["USERS_TO_PING"], quote=False)


def webhook(request):
    bot = Bot(token=os.environ["TELEGRAM_TOKEN"])
    dispatcher = Dispatcher(bot, None, 0)
    dispatcher.add_handler(CommandHandler("cs", cs_callback))

    if request.method == "POST":
        update = Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
    return "ok"
