import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page = request.GET.get('page', 1)
    data = list()

    with open(BUS_STATION_CSV, encoding='utf8') as raw_data:
        reader = csv.DictReader(raw_data)
        for row in reader:
            data.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})

    paginator = Paginator(data, 10)
    stations = paginator.get_page(page)
    context = {
         'page': stations,
    }

    return render(request, 'stations/index.html', context)
