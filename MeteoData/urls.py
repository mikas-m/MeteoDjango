from django.urls import path
from .views import MeteoDataListView

urlpatterns = [
    path('', MeteoDataListView, name='meteo-detail'),
]
