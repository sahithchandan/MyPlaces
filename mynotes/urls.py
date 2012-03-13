from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('mynotes.views',
    url(r'^register/$', 'user_registration', name='registration'),
    url(r'^add-note/$', 'add_note', name='add_note'),
    url(r'^$', 'home', name='home'),
)