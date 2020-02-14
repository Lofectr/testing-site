from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('index.urls')),
    path('auth/', include('login.urls')),
    path('administrator/', include('administrator.urls')),
    path('admin/', admin.site.urls),
    path('regTeacher/', include('regTeacher.urls')),
    path('curator/', include('curatorPanel.urls')),
    path('create-ref-for-testing/', include('createRefForTesting.urls'))
]
