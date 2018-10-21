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
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    pub_date = models.DateField()
    word_count = models.IntegerField()
    price = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=64)


class Token(models.Model):
    value = models.CharField(max_length=64)  # session_key
    user = models.OneToOneField(UserInfo)  # 只能登陆一次，再次登陆则会重新生成token值


