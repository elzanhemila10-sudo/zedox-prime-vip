from loader import bot
from utils import *
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton

@bot.message_handler(commands=["start"])
def start(m):
    uid=m.from_user.id
    ensure_user(uid)

    bot.send_message(m.chat.id,
    "🎉 *Zedox Prime VIP*\n\n💰 Points: "+str(get_points(uid)),
    parse_mode="Markdown",
    reply_markup=main_menu(uid))
