from typing import Final
from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes
from openai import OpenAI
client = 'Insert API Key Here'

chat_history = [{"role": "system", "content": "You are friend that is helping them to learn korean currently graded at C9. you only speak in korean"}]
conversation = []
TOKEN:Final = 'Insert Bot Token Here'

BOT_USERNAME: Final='Insert Bot Name Here'

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

    chat_history.append({"role": "user", "content": text})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat_history
    )

    reply = response.choices[0].message.content.strip()
    response:str = handle_response(text)
    print('BOT: ', reply)
    await update.message.reply_text(reply)

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
    app.run_polling(poll_interval=0.0)