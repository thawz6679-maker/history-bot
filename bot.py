import telebot

TOKEN = '9081731422:AAHBAMgcJXQcrMBNvZ6ky8hHr0AQyTdUIP4'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "မင်္ဂလာပါခင်ဗျာ။ သမိုင်းနှင့် စာပေ Bot မှ ကြိုဆိုပါတယ်။ 🌟")

bot.infinity_polling()
