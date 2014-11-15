from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eros.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^addcourse/$', include('core.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'core/login.html'}),
    url(r'^', include('core.urls')),
)
