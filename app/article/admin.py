from django.contrib import admin
from django.contrib.auth.models import Group

from app.article.models import *


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'draft', 'date', 'scheduled_date', 'url',)


class HistoryArticleTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'article',)


admin.site.unregister(Group)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(HistoryArticleTask, HistoryArticleTaskAdmin)
