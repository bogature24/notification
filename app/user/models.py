from django.db import models

from app.article.models import Category


class TelegramChat(models.Model):
    user_id = models.CharField(max_length=200)

    def __str__(self):
        return self.user_id


class CategoryArticleTelegramChat(models.Model):
    chat = models.ForeignKey(TelegramChat, null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
