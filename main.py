import logging
import requests
from telegram.ext import Updater, CommandHandler
from telegram import ReplyKeyboardMarkup, Bot


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)',
    level=logging.INFO)

Telegram_token = '7189109603:AAFF0hyVp8yH_8Cy-cuQGEaShaVLkN9afOE'


def get_data():
    try:
        response = requests.get('')
    except Exception as error:
        logging.error(f'Ошибка при запросе к основному API: {error}')
        new_url = None
        response = requests.get(new_url)
    response = response.json()
    return response


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([['Узнать курс валют', 'Спросить о чем-то']], resize_keyboard=True)
    context.bot.send_message(chat_id=chat.id,
                             text='Привет, {}. Этот чат бот ЦБ РФ поможет тебе по всем интересующим тебя вопросам!'.format(
                                 name),
                             reply_markup=button)


def main():
    updater = Updater(token=Telegram_token)
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.start_polling(poll_interval=10.0)
    updater.idle()


if __name__ == '__main__':
    main()
