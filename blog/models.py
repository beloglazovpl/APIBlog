from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Article(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название статьи')
    text = models.TextField(verbose_name='Текст статьи')

    def __str__(self):
        return self.name


class Comment(MPTTModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария')
    text = models.TextField(verbose_name='Текст комментария')
    publish = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время комментария')

    class MPTTMeta:
        order_insertion_by = ['publish']

    def __str__(self):
        return f'Комментарий {self.tree_id}_{self.id}'
