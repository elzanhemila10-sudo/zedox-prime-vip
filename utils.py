import json,os,time
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton

USERS="users.json"

def load():
    if not os.path.exists(USERS):
        open(USERS,"w").write("{}")
    return json.load(open(USERS))

users=load()

def save():
    json.dump(users,open(USERS,"w"),indent=4)

def ensure_user(uid):
    uid=str(uid)
    if uid not in users:
        users[uid]={"points":0}
        save()

def get_points(uid):
    ensure_user(uid)
    return users[str(uid)]["points"]

def main_menu(uid):
    k=InlineKeyboardMarkup()
    k.add(InlineKeyboardButton("💰 Balance",callback_data="balance"))
    return k

def admin_menu():
    k=InlineKeyboardMarkup()
    k.add(InlineKeyboardButton("Stats",callback_data="stats"))
    return k
