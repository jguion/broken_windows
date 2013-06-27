from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'boston/?$', 'boston_disorder.views.crm'),
    url(r'boston/physical/(?P<map_type>[a-zA-Z0-9: _]*)/?$', 'boston_disorder.views.crm'),
    url(r'boston/social/(?P<map_type>[a-zA-Z0-9: _]*)/?$', 'boston_disorder.views.calls'),
    url(r'boston/display_map/physical/(?P<map_type>[a-zA-Z0-9: _]*)/?$', 'boston_disorder.views.limited_crm'),
    url(r'boston/display_map/social/(?P<map_type>[a-zA-Z0-9: _]*)/?$', 'boston_disorder.views.limited_calls'),
    url(r'boston/more_info/?$', 'boston_disorder.views.more_info')

)
