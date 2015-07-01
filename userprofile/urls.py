from django.conf.urls import patterns, url
from userprofile import views


urlpatterns = patterns('',
        url(r'^$', views.roster, name='roster'),
        url(r'^update_profile/$', views.update_profile, name='update_profile'),
        #url(r'^profile/(?P<profile_id>\d+)/$', views.profile, name='profile'),
        #url(r'^your_profile/$', views.your_profile, name='your_profile'),
)
