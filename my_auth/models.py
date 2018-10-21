from django.db import models

import datetime

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=64)
    create_time = models.DateTimeField(default=datetime.datetime.now)
    user_type = models.IntegerField(choices=((0,'工作人员'),(1,'消费者')), default=1)

    def __str__(self):
        return self.username


class Token(models.Model):
    value = models.CharField(max_length=64)  # session_key
    user = models.OneToOneField(UserInfo)  # 只能登陆一次，再次登陆则会重新生成token值
    create_time = models.DateTimeField(default=datetime.datetime.now)

