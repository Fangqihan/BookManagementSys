from rest_framework import serializers
from .models import Publisher, Author, Book, Comment


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'
        depth = 1


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # depth = 1  # 此物是个祸害，尽量少用

    # def create(self, validated_data):
    #     print('validated_data>>>>>>>', validated_data)
    #     authors = validated_data.pop('authors')
    #     obj = Book.objects.create(**validated_data)
    #     obj.authors.add(*authors)
    #     return obj


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        depth = 1


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        depth = 1

