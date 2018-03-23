"""rps_game URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from game.views import (
    BasicView,
    AddUserView,
    UserLoginView,
    UserLogoutView,
    LoggedUserView,
    LobbyView,
    GameView,
    GameRoundView,
    JoinGameView,
    JoinRoundView,
    ResultsView,
    ResultsJoinView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', BasicView.as_view()),
    url('^register/$', AddUserView.as_view(), name="register"),
    url('^login/$', UserLoginView.as_view(), name="login"),
    url('^logout/$', UserLogoutView.as_view(), name="logout"),
    url('^create/$', LoggedUserView.as_view(), name="create"),
    url('^lobby/$', LobbyView.as_view(), name="lobby"),
    url('^game-view/(?P<id>(\d)+)$', GameView.as_view(), name="game_view"),
    url('^game-view/(?P<id>(\d)+)/round/(?P<round_id>(\d)+)$', GameRoundView.as_view(), name="round"),
    url('^join-game/(?P<game_id>(\d)+)$', JoinGameView.as_view(), name="join_game"),
    url('^join-game/(?P<game_id>(\d)+)/round/(?P<round_id>(\d)+)$', JoinRoundView.as_view(), name="join_round"),
    url('^game-view/(?P<game_id>(\d)+)/results/$', ResultsView.as_view(), name="results"),
    url('^join-game/(?P<game_id>(\d)+)/results/$', ResultsJoinView.as_view(), name="results_join"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)