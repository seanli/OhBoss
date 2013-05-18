from django.conf.urls import patterns, url


urlpatterns = patterns('core.views',
    url(r'^$', 'index'),
    url(r'^facebook-login/$', 'facebook_login'),
    url(r'^logout/$', 'logout'),
    url(r'^api/friend/list/$', 'api_friend_list'),
)
