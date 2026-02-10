# sistema_contatos/urls.py
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <h1>🎉 Sucesso! Django está rodando no Render!</h1>
    <p><a href="/admin/">Admin</a></p>
    <p>Status: ✅ Online</p>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]