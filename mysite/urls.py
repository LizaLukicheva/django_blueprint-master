from django.conf.urls import *
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', TemplateView.as_view(template_name='frontpage.html.html'), name='frontpage'),
    url(r'^$', "news.views.index"),
    (r'detail/(\d+)', "news.views.detail"),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

