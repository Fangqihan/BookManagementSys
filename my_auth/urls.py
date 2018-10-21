from django.conf.urls import url
from my_auth.views import LoginView, RegisterView


urlpatterns = [
    url(r'^login/$', LoginView.as_view()),
    url(r'^register/$', RegisterView.as_view()),
]



