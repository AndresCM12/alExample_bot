from telegram.ext import Updater, CommandHandler


def start(update, context):
    update.message.reply_text('Hola:3')


if __name__ == '__main__':
    updater = Updater(token='1640387268:AAEIO5fZ3ykYV7zbcDf7IoHr6jPI3dIEyX4', use_context=True)
    dp = updater.dispatcher

    #add handler
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()
