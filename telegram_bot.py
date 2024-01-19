from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
def start(bot, update):
    update.message.reply_text('Hi! Welcome to join to my channel!\n'
                              'For continue follow to use this instructor', reply_markup=markup)
def close_keyboard(bot, update):
    update.message.reply_text('Ok', reply_markup=ReplyKeyboardRemove())

def echo(bot, update):
    if update.message.text[-1] == '?':
        update.message.reply_text('Of course you can ask! I\'ll just be culturally silent...')
    else :
        update.message.reply_text('Quite possible, who knows?')

def address(bot, update):
    update.message.reply_text('Address: Карши, ул. Жайхун, 31')

def phone(bot, update):
    update.message.reply_text('Phone: +998 99 405 33 00')

def site(bot, update):
    update.message.reply_text('Site: https://yandex.ru/images/search?img_url=https%3A%2F%2Fplay-lh.googleusercontent.com%2FvlFAwOkXvY8AwTdAf_9DqUHaZ11orHiOA9kkNFA1KIbhBxh6ux8pVnVixeMSDM3FklY&lr=10331&pos=3&rpt=simage&source=serp&text=Madina%20pharm%20Qarshi')

def work_time(bot, update):
    update.message.reply_text('Work Time: Whole Weekdays from 09:00 a.m to at 18:00 pm')


updater = Updater('6757506394:AAEO98wZjvlB_53jwRh_LibXJmKsb4RiFwY')

dp = updater.dispatcher

reply_keyboard = [['🔍 Qidirish',
                   '💬 Fikr bildirish', '🔄 Tilni o\`zgartirish',
                   '📍Mening joylashuvim: O\`zbekiston bo\`yicha',
                   'Qanday qo\`llash mumkin❓']]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False, resize_keyboard=True)

dp.add_handler(CommandHandler('start', start))
dp.add_handler(CommandHandler('close', close_keyboard()))
dp.add_handler(CommandHandler('address', address))
dp.add_handler(CommandHandler('phone', phone))
dp.add_handler(CommandHandler('site', site))
dp.add_handler(CommandHandler('work_time', work_time))

textHandler = MessageHandler(Filters.text, echo)
dp.add_handler(textHandler)

updater.start_polling()

updater.idle()
