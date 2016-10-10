from django.conf.urls import url

from football_data import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^leagues/$',
        views.LeagueList.as_view(),
        name='league-list'),
    url(r'^leagues/(?P<pk>[0-9]+)/$',
        views.LeagueDetail.as_view(),
        name='league-detail'),
    url(r'^teams/$',
        views.TeamList.as_view(),
        name='team-list'),
    url(r'^teams/(?P<pk>[0-9]+)/$',
        views.TeamDetail.as_view(),
        name='team-detail'),
    url(r'^stadiums/$',
        views.StadiumList.as_view(),
        name='stadium-list'),
    url(r'^stadiums/(?P<pk>[0-9]+)/$',
        views.StadiumDetail.as_view(),
        name='stadium-detail'),
    url(r'^players/$',
        views.PlayerList.as_view(),
        name='player-list'),
    url(r'^players/(?P<pk>[0-9]+)/$',
        views.PlayerDetail.as_view(),
        name='player-detail'),
    url(r'^matches/$',
        views.MatchList.as_view(),
        name='match-list'),
    url(r'^matches/(?P<pk>[0-9]+)/$',
        views.MatchDetail.as_view(),
        name='match-detail'),
]