from django.urls import path, include
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', InicioView.as_view(), name='home'),
    path('about/', AcercaDeNosotrosView.as_view(), name='about'),
    path('contact/', ContactoView.as_view(), name='contact'),
    path('article/', include('articulos.urls')),
]