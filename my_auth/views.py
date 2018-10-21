from django.views import View
from rest_framework.views import APIView
from rest_framework import generics
from my_auth.models import UserInfo, Token
import uuid
from rest_framework.response import Response


class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        ret = {'code': 1000}
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user_obj = UserInfo.objects.filter(username=username).first()
        if user_obj:
            ret['code'] = 1001
            ret['error'] = "用户名已注册！"
        else:
            UserInfo.objects.create(username=username, password=password)
            ret['msg'] = '恭喜，注册成功。'
        return Response(ret)


def get_token(username):
    """生成token值"""
    import time
    import hashlib
    hash = hashlib.md5(username.encode('utf-8'))
    hash.update(str(time.time()).encode('utf-8'))
    return hash.hexdigest()


class LoginView(APIView):

    def post(self, request):
        """此处若是继承View就会出现跨域错误"""
        ret = {'code': 1000}
        username = request.data.get('username','')
        password = request.data.get('password','')
        user_obj = UserInfo.objects.filter(username=username,password=password).first()
        print(user_obj)
        if not user_obj:
            ret['code'] = 1001
            ret['error'] = "用户名或密码错误"
        else:
            token = str(uuid.uuid4())
            Token.objects.update_or_create(user_id=user_obj.id,defaults={'value':token})
            ret['token']= token
        return Response(ret)




