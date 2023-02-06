from django.urls import path

from app.telegram_bot.views import webhook


urlpatterns = [
    path("", webhook),
]
