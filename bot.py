from loader import bot
import handlers.user
import handlers.admin
import handlers.callbacks

print("🔥 Zedox Prime VIP started")
bot.infinity_polling(skip_pending=True)
