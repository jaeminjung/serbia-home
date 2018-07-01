from django.conf.urls import url
from . import views


# app_name = 'stories'

urlpatterns = [

    url(r'^create/$', views.stories_create, name='stories_create'),
    # url(r'^(?P<p_key>\d+)/', views.stories_detail, name='stories_detail'),
    url(r'^(?P<p_key>[\0-9]+)/$', views.stories_detail, name='stories_detail'),
    url(r'^(?P<p_key>[\0-9]+)/edit/$', views.stories_edit, name='stories_edit'),

    url(r'^(?P<p_key>[\0-9]+)/comment/$', views.add_comment, name='add_comment'),

    url(r'^mylist/$', views.stories_mylist, name='stories_mylist'),
    url(r'^$', views.stories_list, name='stories_list'),
]
