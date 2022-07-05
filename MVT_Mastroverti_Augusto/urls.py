from django.contrib import admin
from django.urls import URLPattern, path
from views import html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('html/', html),
]
