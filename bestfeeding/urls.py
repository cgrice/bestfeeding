from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from feeds.views import home, create, delete, stats

urlpatterns = patterns('',
    # (r'^$', 'reading.views.home')
    # Examples:
    # url(r'^$', 'seymour.views.home', name='home'),
    # url(r'^seymour/', include('seymour.foo.urls')),
    url(
        regex=r'^$',
        view=home,
        name='feeds_home'
    ),
    url(
        regex=r'^new$',
        view=create,
        name='feeds_create'
    ),
    url(
        regex=r'^delete/(?P<feed_id>\d+)$',
        view=delete,
        name='feeds_delete'
    ),
    url(
        regex=r'^stats$',
        view=stats,
        name='feeds_stats'
    ),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()


