from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog', views.catalog, name='catalog'),
    path('profile', views.profile, name='profile'),
    path('vxod', views.vxod, name='vxod'),
    path('catalogod', views.catalogod, name='catalogod'),
    path('catalogteh', views.catalogteh, name='catalogteh'),
]
