from rest_framework import viewsets
from .models import Article
from .serializers import articleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = articleSerializer