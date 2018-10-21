
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import Token


class TokenAuth(BaseAuthentication):
    """自定义验证类"""
    def authenticate(self, request):
        """验证逻辑"""
        token = request._request.GET.get('token' ,'')
        print(token)
        token_obj = Token.objects.filter(value=token).first()

        # 验证失败
        if not token_obj:
            raise AuthenticationFailed('认证失败')

        # 通过验证，返回元祖，表示用户
        return (token_obj.user ,token_obj)

    def authenticate_header(self, request):
        pass


