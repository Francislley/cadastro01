from django.conf.urls import include, url
from profiles import views

urlpatterns = [
  url(r'^$', views.index, name = 'index'),
  url(r'^profiles/(?P<profile_id>\d+)$', views.show, name = 'show_profile'),
  url(r'^profiles/(?P<profile_id>\d+)/invite$', views.invite, name = 'invite'),
  url(r'^invites/(?P<invite_id>\d+)/accept$', views.accept, name = 'accept_invite')
]