from celery import shared_task


@shared_task
def add_task(title, text, image, category_id, url):
    print("!!!!!!!!!! 123")
    print("!!!!!!!!!! 123")
    print("!!!!!!!!!! 123")
    # from app.article.models import CategoryArticleTelegramChat
    # telegram_chat = CategoryArticleTelegramChat.objects.filter(category_id=category_id)
    # print("telegram_chat", telegram_chat)
    #
    # for item in telegram_chat:
    #     print("chat", item.chat.user_id)
    #
    #     if url:
    #         buttons = [
    #             InlineKeyboardButton(
    #                 text="Подробней",
    #                 url=url
    #             ),
    #         ]
    #     else:
    #         buttons = []
    #
    #     send_chunked_message(
    #         user_id=item.chat.user_id,
    #         bot=bot,
    #         buttons=buttons,
    #         chunk=1,
    #         photo=image,
    #         text=f'{title} \n\n {text}'
    #     )

    return "Valid send"