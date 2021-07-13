from .models import *
from .serializers import *
from rest_framework import viewsets, permissions


class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    permission_classes = [ 
        permissions.AllowAny
            ]

    def get_queryset(self):
        print(self.request.user)
        # return Lead.objects.filter(owner = self.request.user)
        return Lead.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)