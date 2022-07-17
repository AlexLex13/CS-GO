from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(PlayersHome.as_view()), name='home'),
    path('about/', about, name='about'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LoginUser.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('player/<slug:player_slug>/', ShowPlayer.as_view(), name='player'),
    path('team/<slug:team_slug>/', PlayerTeam.as_view(), name='team')
]