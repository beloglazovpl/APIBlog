from django.urls import path

from blog.views import ArticlesViewAll, ArticleView, CommentView, AddCommentView

urlpatterns = [
    path('article/', ArticlesViewAll.as_view()),
    path('article/<int:pk>/', ArticleView.as_view()),
    path('comment/', AddCommentView.as_view()),
    path('comment/<int:pk>/', CommentView.as_view()),
]
