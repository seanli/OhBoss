from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('core.views',
    url(r'^$', 'index'),
    url(r'^api/user/register/$', 'api_user_register'),
)
