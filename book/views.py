from .models import Publisher, Book, Author
from .my_serializers import PublisherSerializer, AuthorSerializer, BookSerializer
from rest_framework import viewsets
from rest_framework.authentication import BaseAuthentication
from my_auth.auth import TokenAuth


class AuthView(BaseAuthentication):
    authentication_classes = [TokenAuth,]


class PublisherView(AuthView, viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class BookView(AuthView,viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorView(AuthView,viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer



