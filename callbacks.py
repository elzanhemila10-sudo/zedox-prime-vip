from loader import bot
from utils import *

@bot.callback_query_handler(func=lambda c:True)
def cb(c):
    if c.data=="balance":
        bot.send_message(c.message.chat.id,
        "💰 Points: "+str(get_points(c.from_user.id)))
