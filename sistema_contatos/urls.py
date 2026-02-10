# sistema_contatos/urls.py
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("🚀 Django 6.0 rodando no Render!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]