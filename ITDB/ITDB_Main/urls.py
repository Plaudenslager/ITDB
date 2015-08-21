from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /main/
    url(r'^$', views.index, name='index'),
    # ex: /main/theater/
    url(r'^theater/$', views.theaters, name='theaters'),
    # ex: /main/theater/1/
    url(r'^theater/(?P<theater_id>[0-9]+)/$', views.theater_detail, name='theaters'),
    # ex: /main/production/
    # ex: /main/production/1
    url(r'^production/(?P<production_id>[0-9]+)/$', views.production_detail, name='productions'),
    # ex: /main/people/
    url(r'^people/$', views.people, name='people'),
    # ex: /main/people/1
    # ex: /main/play/
    url(r'^play/$', views.plays, name='plays'),
    # ex: /main/play/1
    url(r'^play/(?P<play_id>[0-9]+)/$', views.play_detail, name='plays'),

]
