from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    #/music/
    url(r'^$', views.index, name='index'),

    # music/71/
    url(r'^(?P<album_id>[0-9]+)/$', views.details,name='detail'),
    #music/album_id/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

    url(r'^lista/', views.list, name='list')

]