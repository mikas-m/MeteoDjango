from .models import MeteoData
from django.shortcuts import render



def MeteoDataListView(request):
    meteo_data = MeteoData.objects.all()
    return render(request, "meteo_data_detail.html", {"meteo_data": meteo_data})