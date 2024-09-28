from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from .import fb


urlpatterns = [
    path('admin/', admin.site.urls),
    path('kannadaprabha/', fb.kannadaprabha.fb),
   
]
 