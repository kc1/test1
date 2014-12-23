from django.conf.urls import patterns, include, url
from django.contrib import admin

from app1.views import index

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index/', 'app1.views.index', name='index'),
    url(r'^contact/$', 'app1.views.contact', name='contact'),

    url(r'^admin/', include(admin.site.urls)),
)



