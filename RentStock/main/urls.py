from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('catalog', views.catalog, name='catalog'),
    path('profile', views.profile, name='profile'),
    path('vxod', views.vxod, name='vxod'),
    path('catalog2', views.catalog2, name='catalog2'),
    path('catalog3', views.catalog3, name='catalog3'),
]
