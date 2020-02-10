from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('index.urls')),
    path('auth/', include('login.urls')),
    path('administrator/', include('administrator.urls')),
    path('admin/', admin.site.urls),
]
