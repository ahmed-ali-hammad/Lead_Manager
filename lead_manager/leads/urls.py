from django.urls import path 
from rest_framework import routers
from .views import *

app_name = 'leads'

router = routers.DefaultRouter()
router.register (r'leads', LeadViewSet, basename = 'leads')

urlpatterns = router.urls