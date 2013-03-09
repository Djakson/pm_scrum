from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.staticfiles.templatetags import staticfiles
from pm_scrum import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile/', include('user_profile.urls')),
    url(r'', include('projects.urls')),
    url(r'^avatar/', include('avatar.urls')),
)

