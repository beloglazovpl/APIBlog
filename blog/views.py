from rest_framework.generics import ListCreateAPIView, get_object_or_404, RetrieveAPIView

from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer, CommentCreateSerializer


class ArticlesViewAll(ListCreateAPIView):
    """Получить список статей / создать новую статью"""
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer

    def article_create(self, serializer):
        article = get_object_or_404(
            Article,
            name=self.request.data.get('name'),
            text=self.request.data.get('text')
        )
        return serializer.save(article=article)


class AddCommentView(ListCreateAPIView):
    """Добавить комментарий"""
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

    def comment_create(self, serializer):
        comment = get_object_or_404(
            Comment,
            article=self.request.data.get('article'),
            author=self.request.data.get('author'),
            text=self.request.data.get('text'),
            parent=self.request.data.get('parent')
        )
        return serializer.save(comment=comment)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# реализовать вывод комментариев до 3 уровня вложенности не удалось
class ArticleView(RetrieveAPIView):
    """Вывод статьи с комментариями"""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentView(RetrieveAPIView):
    """Получение всех комментариев для выбранного комментария 3 уровня"""
    queryset = Comment.objects._mptt_filter(level=3)
    serializer_class = CommentSerializer
