import telegram
from telegram import InlineKeyboardMarkup, InputMediaPhoto, InputMediaDocument
from telegram.ext import CallbackContext


BACK_BUTTON = "Назад"


def chunks(lst: list, n: int):
    for i in range(0, len(lst), n):
        yield lst[i: i + n]


def remove_last_message(context: CallbackContext):
    try:
        context.bot.delete_message(
            context.chat_data["id"], context.user_data["last_message_id"]
        )
    except:
        pass


def remove_message(context: CallbackContext):
    try:
        context.bot.delete_message(
            context.user_data["chat_id"], context.user_data["message_id"]
        )
    except:
        pass


def remove_last_message_by_message_id(context, message_id):
    try:
        context.bot.delete_message(
            context.chat_data["id"], message_id
        )
    except:
        pass


def remove_last_inline_messages(context: CallbackContext):
    if "last_messages_ids" not in context.user_data:
        return
    for message_id in context.user_data["last_messages_ids"]:
        try:
            context.bot.delete_message(context.chat_data["id"], message_id)
        except:
            pass
    context.user_data["last_messages_ids"].clear()


def send_chunked_message(
        user_id,
        bot,
        buttons: list,
        photo=None,
        text: str = "...",
        limit: int = 45,
        chunk: int = 3,
):

    if len(buttons) > limit:
        first = True
        for x in range(0, len(buttons), limit):
            reply_markup = InlineKeyboardMarkup(
                list(chunks(buttons[x: x + limit], chunk))
            )
            if first and photo:
                bot.send_photo(
                    user_id,
                    reply_markup=reply_markup,
                )
            else:
                bot.send_message(
                    user_id,
                    text=text,
                    reply_markup=reply_markup,
                )
            first = False
    else:
        if photo:
            bot.send_photo(
                user_id,
                photo,
                caption=text,
                reply_markup=InlineKeyboardMarkup(list(chunks(buttons, chunk))),
            )
        else:
            bot.send_message(
                user_id,
                text=text,
                reply_markup=InlineKeyboardMarkup(list(chunks(buttons, chunk))),
            )


def send_prepared_post(
        resource_id,
        bot,
        title,
        text,
        photos=None
):
    media_group = []
    if text:
        text = f'<b>{title}</b>\n{text}'
    else:
        text = f'<b>{title}</b>'
    i = 0
    for photo in photos:
        media_group.append(InputMediaPhoto(photo.photo,
                                           caption=text if i == 0 else '', parse_mode=telegram.ParseMode.HTML))
        i += 1
    if media_group:
        bot.send_media_group(chat_id=resource_id, media=media_group)
    else:
        bot.send_message(chat_id=resource_id, text=text, parse_mode=telegram.ParseMode.HTML)


def send_file_message(

        user_id,
        bot,
        context=None,
        photos=None,
        document=None,
        reply_markup=None,
        text: str = "...",
):
    media_group = []
    i = 0
    for photo in photos:
        media_group.append(InputMediaPhoto(photo.photo,
                                           caption=text if i == 0 else '', parse_mode=telegram.ParseMode.HTML)
                           )
        i += 1
    if document:
        media_group.append(InputMediaDocument(media=document, caption=text, parse_mode=telegram.ParseMode.HTML))
    if media_group:
        bot.send_media_group(
            user_id,
            media=media_group,
            reply_markup=reply_markup
        )
    else:
        bot.send_message(
            user_id,
            text=text,
        )

data_dict = {
    "goal_pk": None
}

def send_message(user_id, bot, text):
    bot.send_message(user_id,
                     text=text,
                     parse_mode=telegram.ParseMode.HTML)