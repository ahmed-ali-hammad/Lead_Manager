from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('leads.urls', namespace = 'lead')),
    path('accounts/', include('accounts.urls', namespace = 'accounts' )),
    path('', include('frontend.urls', namespace = 'frontend')),
    
]
