from django.conf.urls import include, url

urlpatterns = [
  url(r'^$', 'profiles.views.index', name = 'index'),
  url(r'^profiles/(?P<profile_id>\d+)$', 'profiles.views.show', name = 'show_profile')
]