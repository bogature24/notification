from django.contrib import admin

from app.user.models import TelegramChat, CategoryArticleTelegramChat


class TelegramChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id',)


class CategoryArticleTelegramChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat', 'category',)


admin.site.register(TelegramChat, TelegramChatAdmin)
admin.site.register(CategoryArticleTelegramChat, CategoryArticleTelegramChatAdmin)
