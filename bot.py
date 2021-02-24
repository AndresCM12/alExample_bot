import qrcode
import os
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from telegram import ChatAction
INPUT_TEXT = 0

#un función para enviar un saludo
def start(update, context):
    chat = update.message.chat
    chat.send_action(
        action= ChatAction.TYPING,
        timeout=None
    )
    update.message.reply_text('Hola:3')

def qr_command_handler(update, context):

    update.message.reply_text('Envía el texto que quieras convertir a un código QR')

    return INPUT_TEXT

def generate_qr(text):
    filename = text + '.jpg'
    img = qrcode.make(text)
    img.save(filename)

    return filename

#obtenemos el texto que esta introduciendo el usuario
def input_text(update, context):

    text = update.message.text


    filename = generate_qr(text)
    chat = update.message.chat
    send_qr(filename, chat)


    return ConversationHandler.END

def send_qr(filename, chat):
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )

    chat.send_photo(
        photo=open(filename, 'rb')
    )
    os.unlink(filename)

if __name__ == '__main__':

    updater = Updater(token='1640387268:AAEIO5fZ3ykYV7zbcDf7IoHr6jPI3dIEyX4', use_context=True)

    dp = updater.dispatcher

    #llama al método si le introducen el comando start
    dp.add_handler(CommandHandler('start', start))

    #iniciamos una conversacion, con entradas y sus estados, en este caso empiezan cuando utilizamos el comandop qr
    dp.add_handler(ConversationHandler(

        entry_points=[

            CommandHandler('qr', qr_command_handler)
        ],

        states={
            #en caso de que el estado sea cero, llamamos despues de filtar el texto a la funcion input text
            INPUT_TEXT: [MessageHandler(Filters.text, input_text)]
        },

        fallbacks=[]
    ))

    #hacemos un ciclo para que siempre esté escuchando lo que le envían
    updater.start_polling()

    updater.idle()
