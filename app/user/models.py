from django.db import models


class TelegramChat(models.Model):
    user_id = models.CharField(max_length=200)

    def __str__(self):
        return self.user_id
