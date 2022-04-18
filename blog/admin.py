from django.contrib import admin
from blog.models import *
from mptt.admin import MPTTModelAdmin


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'text']


admin.site.register(Comment, MPTTModelAdmin)
