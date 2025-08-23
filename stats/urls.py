from django.urls import path
from . import views
# Defines URL patterns for the \'stats\' application.
urlpatterns = [
    # Maps the root URL of the app to the \'index\' view.
    path('', views.index, name='index'),
    # Maps \'/api/top-players/\' to the \'top_players_api\' view for API access.
    path('api/top-players/', views.top_players_api, name='top_players_api'),
]