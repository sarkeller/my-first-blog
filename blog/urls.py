from django.conf.urls import url
from . import views

#adding URL pattern
urlpatterns= [
    url(r'^$', views.post_list, name='post_list'),
]
