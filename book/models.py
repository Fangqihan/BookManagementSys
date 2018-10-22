from django.db import models


class Publisher(models.Model):
    title = models.CharField(max_length=32)
    address = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=32)
    birth_date = models.DateField()
    gender = models.IntegerField(choices=((0,'male'),(1,'female')),default=0)
    email = models.EmailField(max_length=64)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=32)
    authors = models.ManyToManyField("Author")
    publisher = models.ForeignKey('Publisher')
    pub_date = models.DateField()
    word_count = models.IntegerField()
    price = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.title


from my_auth.models import UserInfo
import datetime

class Comment(models.Model):
    content = models.CharField(max_length=128)
    user = models.ForeignKey(UserInfo)
    book = models.ForeignKey(Book)
    create_time = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return '%s/%s/%s/%s' % (self.content,self.create_time,self.book.title, self.user.username)


class Score(models.Model):
    balance = models.IntegerField(default=0)
    user = models.OneToOneField(UserInfo)

    def __str__(self):
        return '用户<%s> 积分<%s>'%(self.user.username, self.balance)

