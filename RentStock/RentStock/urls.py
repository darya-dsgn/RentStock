from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('catalog/', include('main.urls')),
    path('catalogod/', include('main.urls')),
    path('catalogteh/', include('main.urls')),
    path('user/', include('users.urls', namespace='user')),
]
