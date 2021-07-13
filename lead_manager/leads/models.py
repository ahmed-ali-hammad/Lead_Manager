from django.contrib.auth.models import User
from django.db import models

class Lead(models.Model):
    owner = models.ForeignKey(User, related_name = "leads", on_delete=models.CASCADE, null = True)
    name = models.CharField (max_length = 100)
    email = models.EmailField (max_length = 100 , unique = True)
    message = models.CharField (max_length = 500, blank = True)
    created_at = models.DateTimeField (auto_now_add = True )
    
    def __str__(self):
        return self.name
