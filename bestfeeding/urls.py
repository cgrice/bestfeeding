from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from feeds.views import home, delete

urlpatterns = patterns('',
    # (r'^$', 'reading.views.home')
    # Examples:
    # url(r'^$', 'seymour.views.home', name='home'),
    # url(r'^seymour/', include('seymour.foo.urls')),
    url(
        regex=r'^$',
        view=home,
        name='feed_create'
    ),
    url(
        regex=r'^delete/(?P<feed_id>\d+)$',
        view=delete,
        name='feed_delete'
    ),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()


