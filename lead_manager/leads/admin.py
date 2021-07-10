from django.contrib import admin
from .models import *


class LeadAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Lead, LeadAdmin)

# admin.site.register(Lead)
