from .models import Publisher, Book, Author, Comment
from .my_serializers import PublisherSerializer, AuthorSerializer, BookSerializer, CommentSerializer
from rest_framework import viewsets
from my_auth.auth import TokenAuth
from my_auth.permissions import MyPermission


class AuthView:
    authentication_classes = [TokenAuth,]


class PermissionView:
    permission_classes = [MyPermission,]


class PublisherView(AuthView, PermissionView, viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import HttpResponse



class AuthorView(AuthView, PermissionView, viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


