"""juegos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from game.views import ApiDesarrolladora, ApiJuego, ApiJuegos2
from frontend.views import home_juegos, v_juegos, v_juego,v_update

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/desarrolladora/$', ApiDesarrolladora.get_all_developers),
    url(r'^api/desarrolladora/new', ApiDesarrolladora.create),
    url(r'^api/desarrolladora/(?P<id>[0-9]+)/$', ApiDesarrolladora.manage_by_id),
    url(r'^api/juegos/$', ApiJuego.get_games),
    url(r'^api/juegos/new', ApiJuego.create_game),
    url(r'^api/juegos/(?P<id>[0-9]+)/$', ApiJuego.manage_game_by_id),
    url(r'^api/games/$', ApiJuegos2.as_view(),name="Api Juegos"),
    url(r'^$', home_juegos, name="home"),
    url(r'^juegos/', v_juegos, name="juegos"),
    url(r'^detalles/(?P<id>[0-9]+)/$', v_juego, name="detalles"),
    url(r'^actualizar/(?P<id>[0-9]+)/$', v_update, name="update"),




]
