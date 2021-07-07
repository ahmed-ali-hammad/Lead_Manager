from .models import *
from .serializers import *
from rest_framework import viewsets, permissions


class LeadViewSet(viewsets.ModelViewSet):
    print('call done')
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [ 
        permissions.AllowAny
            ]