from loader import bot
from utils import *
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton
from config import ADMIN_ID

@bot.message_handler(commands=["settings"])
def admin(m):
    if m.from_user.id!=ADMIN_ID:return
    bot.send_message(m.chat.id,"⚙ ADMIN PANEL",reply_markup=admin_menu())
