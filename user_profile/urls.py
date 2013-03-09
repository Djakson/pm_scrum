from django.conf.urls import url, patterns, include

__author__ = 'djakson'


urlpatterns = patterns('',

    url(r'^$', 'user_profile.views.profile', name='profile'),
    url(r'^message/compose$', 'user_profile.views.send_message', name='send_message'),
    url(r'^message/$', 'user_profile.views.messages', name='user_messages'),
)

