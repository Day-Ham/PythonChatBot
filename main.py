from typing import Final
from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes


TOKEN:Final = '7762935962:AAERpZ846viV9cXZJj8DLug25IWsQzBsooM'

BOT_USERNAME: Final='@Daelingo_bot'

async def start_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hey You Look lonely I can fix that by being your friend :D')

async def help_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Get Some Help')

async def custom_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Custom Command Test')

#Handle Responses

def handle_response(text:str)-> str:
    proccessed:str = text.lower()

    if 'hello' in text:
        return 'Hi!'
    if 'i love you' in text:
        return 'um taken'
    return 'you talking gibberish'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type:str =update.message.chat.type
    text: str =update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text:str =text.replace(BOT_USERNAME, '').strip()
            response:str = handle_response(new_text)
        else:
            return 
    else:
        response:str = handle_response(text)
    print('BOT: ', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__=='__main__':
    print('Starting Bot')
    app = Application.builder().token(TOKEN).build()

    #Commands
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))


    #Messages
    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    #Errors
    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)