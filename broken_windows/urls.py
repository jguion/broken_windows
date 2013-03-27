from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'broken_windows.views.home', name='home'),
    # url(r'^broken_windows/', include('broken_windows.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
     url(r'boston/crm/(?P<l1>[a-zA-Z0-9: _]*)/?$', 'boston_disorder.views.crm'),

)
