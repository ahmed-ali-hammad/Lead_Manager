from django.urls import path, include
from knox import views as knox_views
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('auth/', include('knox.urls')),
    path('register/', UserRegisterAPIView.as_view() , name = "register"),
    path('login/', UserLoginAPIView.as_view(), name = "login"),
    path('logout/', knox_views.LogoutView.as_view(), name = "logout"),
    path('user/', UserAPIView.as_view(), name = "user"),
]
