from rest_framework import serializers
from .models import Publisher, Author, Book, Comment


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'
        depth = 1


class BookSerializer(serializers.ModelSerializer):
    publisher = serializers.IntegerField(source='publisher.pk')

    class Meta:
        model = Book
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        print('validated_data>>>>>>>', validated_data)
        '''
        {
            'title': '钢铁是怎样炼成的',
            'pub_date': datetime.date(2012, 12, 12),
            'word_count': 12, 'price': 29,
            'publisher': <Publisher: 长江出版社>,
            'authors': [<Author: 蒋勋>, <Author: 易中天>]
        }
        '''
        book_obj = Book.objects.create(
            title=validated_data['title'],
            pub_date=validated_data['pub_date'],
            word_count=validated_data['word_count'],
            publisher_id=validated_data['publisher']['pk'],  # 注意此处字段名称为publisher_id！！！
            price=validated_data['price'],
        )
        print('book_obj', book_obj)

        # authors = validated_data.pop('authors')
        # obj = Book.objects.create(**validated_data)
        # book_obj.authors.add(*validated_data['authors'])
        return book_obj



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

