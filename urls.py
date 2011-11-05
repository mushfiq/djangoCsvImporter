from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'csv_importer.views.home', name='home'),
    # url(r'^csv_importer/', include('csv_importer.foo.urls')),
    url(r'^index', 'csv_importer.topic_importer.views.index'),
    url(r'^test', 'csv_importer.topic_importer.views.test'),
    url(r'^file_upload', 'csv_importer.topic_importer.views.file_upload'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
   ) + urlpatterns
