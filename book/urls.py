from django.conf.urls import url,include
from book.views import PublisherView, BookView, AuthorView


urlpatterns = [
    url(r'^v1/publishers/$', PublisherView.as_view({"get":"list","post":"create"})),
    url(r'^v1/publishers/(?P<pk>\d+)/$', PublisherView.as_view(
        {"get":'retrieve',"put":"update","delete":"destroy"}
    )),

    url(r'^v1/books/$', BookView.as_view({"get":"list","post":"create"})),
    url(r'^v1/books/(?P<pk>\d+)/$', BookView.as_view(
        {"get":'retrieve',"put":"update","delete":"destroy"}
    )),

    url(r'^v1/authors/$', AuthorView.as_view({"get":"list","post":"create"})),
    url(r'^v1/authors/(?P<pk>\d+)/$', AuthorView.as_view(
        {"get":'retrieve',"put":"update","delete":"destroy"}
    )),
]

