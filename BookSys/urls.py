from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('book.urls'),),
    url(r'^api/auth/', include('my_auth.urls')),
]




