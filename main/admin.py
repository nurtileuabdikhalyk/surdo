from django.contrib import admin
from .models import Dictionary, Question, News, Users, QuesModel, Result


@admin.register(Dictionary)
class DictionaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'url_youtube')
    list_display_links = ('id', 'word')
    prepopulated_fields = {'slug': ('word',)}


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'email')
    list_display_links = ('id', 'first_name', 'email')
    search_fields = ('first_name', 'email', 'message')
    list_filter = ('created',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name', 'status_admin',)
    list_display_links = ('id', 'user', 'first_name', 'last_name')
    list_editable = ('status_admin',)


@admin.register(QuesModel)
class QuesModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer')
    list_display_links = ('id', 'question', 'answer')


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'score', 'correct', 'incorrect')
    list_display_links = ('id', 'user',)
