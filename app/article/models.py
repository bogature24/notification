
import pytz
from django.db import models
from telegram import InlineKeyboardButton

from app.article.utils import get_photo_link
from app.telegram_bot.config import send_chunked_message
from app.telegram_bot.bot import bot
from app.user.models import TelegramChat


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    text = models.TextField()
    url = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    scheduled_date = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    image_url = models.URLField(blank=True, null=True)
    draft = models.BooleanField(default=True)
    task_id = models.CharField(max_length=200, blank=True, null=True)
    revoke = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @staticmethod
    def send_article_message(article, user_id):

        if article.url:
            buttons = [
                InlineKeyboardButton(
                    text="Подробней",
                    url=article.url
                ),
            ]
        else:
            buttons = []

        send_chunked_message(
            user_id=user_id,
            bot=bot,
            buttons=buttons,
            chunk=1,
            photo=article.image_url,
            text=f'{article.title} \n\n {article.text}'
        )

    def save(self, *args, **kwargs):
        try:
            if not self.image_url:
                image_bytes = self.image.read()
                link = get_photo_link(image_bytes)
                self.image_url = link
            super().save(*args, **kwargs)
            if not self.draft:
                self.send_article_message(self, "385981199")
        except:
            super().save(*args, **kwargs)

        if self.scheduled_date and (self.task_id == "" or self.task_id == None):
            print("start 123")
            from app.article.tasks import add_task
            task = add_task.apply_async((self.title, self.text, self.image_url, self.category.id, self.url), eta=pytz.timezone('Europe/Moscow').localize(self.scheduled_date))
            Article.objects.filter(id=self.id).update(task_id=str(task.task_id))

        # elif self.task_id != None and len(self.task_id) > 0 and self.revoke:
        #
        #     from celery.worker.control import revoke
        #     revoke(task_id=self.task_id, terminate=True, state='PROGRESS')
        #     Article.objects.filter(id=self.id).update(task_id=str(""), revoke=False)


class HistoryArticleTask(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CategoryArticleTelegramChat(models.Model):
    chat = models.ForeignKey(TelegramChat, null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
