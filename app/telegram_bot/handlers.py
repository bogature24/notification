from telegram import Update
from app.telegram_bot.messages import open_start, open_bottom_menu, open_settings_category
from app.user.models import TelegramChat


def start_handler(update: Update, context) -> None:
    user_id = update.message.from_user.id

    if not TelegramChat.objects.filter(user_id=str(user_id)).exists():
        chat = TelegramChat(user_id=str(user_id))
        chat.save()

    open_start(user_id, context)
    open_bottom_menu(user_id, context)


def main_offer(update: Update, context) -> None:
    user_id = update.message.from_user.id

    message = update.message.text
    if "Настройки" in message:
        open_settings_category(user_id, context)
