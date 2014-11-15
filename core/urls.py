from django.conf.urls import patterns, url

from core import views

urlpatterns = patterns('',
    url(r'^addcourse/$', views.addCourseForm, name='addCourseForm'),
    url(r'^$', views.index, name='index'),
)
