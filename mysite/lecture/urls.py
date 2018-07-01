from django.conf.urls import url
from . import views


# app_name = 'stories'

urlpatterns = [
    url(r'^$', views.lecture_notes, name='lecture_notes'),
    url(r'^uploads/$', views.lecture_uploaded, name='lecture_upload'),

]
