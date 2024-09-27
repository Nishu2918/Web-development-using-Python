
from django.shortcuts import render


def loadabout(request):
    return render(request, 'about.html',{"principal_name":'Bindu A Thomas '})

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loadabout/', loadabout)
]