from django.conf.urls import patterns, url

from core import views

urlpatterns = patterns('',
    url(r'^addcourse/$', views.addCourseForm, name='addCourseForm'),
    url(r'^addcourseaction/$', views.addCourse, name='addCourse'),
    url(r'^viewcourse/(?P<course_id>[A-Z ]{4}[0-9]{3}[A-Z]?)/$', views.viewCourse, name='viewCourse'),
    url(r'^addcoursereview/(?P<course_id>[A-Z ]{4}[0-9]{3}[A-Z]?)/$', views.addReviewForm, name='addReviewForm'),
    url(r'^$', views.index, name='index'),
)
