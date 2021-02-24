from telegram.ext import Updater, CommandHandler


def start(update, context):
    update.message.reply_text('Hola:3')


if __name__ == '__main__':
    updater = Updater(token='yourtoken', use_context=True)
    dp = updater.dispatcher

    #add handler
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()
