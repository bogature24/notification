import json

from django.shortcuts import get_object_or_404
from telegram import KeyboardButton, ReplyKeyboardMarkup, Update, InlineKeyboardButton, InlineKeyboardMarkup

from app.article.models import Category, CategoryArticleTelegramChat
from app.telegram_bot.bot import bot
from app.telegram_bot.config import remove_message, send_chunked_message
from app.user.models import TelegramChat


def open_start(user_id: int, context) -> None:
    bot.send_message(
        user_id,
        text=" 😊 Start",
    )


def open_bottom_menu(user_id: int, context) -> None:
    list_btn_row_1 = [
        [KeyboardButton(" ✍️ Настройки", callback_data='settings')],
    ]
    keyboard = ReplyKeyboardMarkup(list_btn_row_1, True)
    bot.send_message(
        user_id,
        reply_markup=keyboard,
        text="✌️ Menu: ",
    )


def check_menu(update: Update, context) -> None:
    user_id = update.callback_query.message.chat.id
    date = update.callback_query.data
    if "unsubscribe_category_" in date:
        id_category = date.replace("unsubscribe_category_", "")
        CategoryArticleTelegramChat.objects.filter(category_id=id_category, chat__user_id=user_id).delete()
        open_settings_category(user_id, context)

    elif "subscribe_category_" in date:
        id_category = date.replace("subscribe_category_", "")

        new_obj = CategoryArticleTelegramChat()
        new_obj.chat = get_object_or_404(TelegramChat, user_id=user_id)
        new_obj.category_id = id_category
        new_obj.save()

        open_settings_category(user_id, context)


def open_settings_category(user_id: int, context) -> None:
    active_category = list(CategoryArticleTelegramChat.objects.filter(chat__user_id=user_id).values_list("category_id", flat=True))

    keyboard = []

    for item in Category.objects.all():

        button = InlineKeyboardButton("❌ Отписаться", callback_data=f'unsubscribe_category_{item.id}') if item.id in active_category \
            else InlineKeyboardButton("✅ Подписаться", callback_data=f'subscribe_category_{item.id}')

        keyboard.append(
            [
                InlineKeyboardButton(item.name, callback_data=f'application_1'),
                button
            ]
        )

    reply_markup = InlineKeyboardMarkup(keyboard)
    message = bot.send_message(
        user_id,
        reply_markup=reply_markup,
        text="Category:"
    )

    remove_message(context)

    context.user_data["chat_id"] = message.chat_id
    context.user_data["message_id"] = message.message_id
