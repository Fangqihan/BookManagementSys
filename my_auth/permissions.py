from rest_framework.permissions import BasePermission

class MyPermission(BasePermission):
    message =  '无权限访问'  # 定制错误信息

    def has_permission(self, request, view):
        # 已经过认证
        user = request.user
        print('请求方法>>> ', request._request.method)
        if user:
            print(user.user_type)
            # 客户只能访问get
            if user.user_type == 1 and request._request.method in ['PUT', 'POST','DELETE']:
                return False
            else:
                return True

