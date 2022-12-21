from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^peliculas/$', views.FilmListView.as_view(), name='film'),
    url(r'directors/$', views.DirectorListView.as_view(),  name='directors')
]