from django.contrib import admin
from django.urls import path, include
from MVT_Mastroverti_Augusto.views import html


urlpatterns = [
    path('admin/', admin.site.urls),
    path('html', html),
]