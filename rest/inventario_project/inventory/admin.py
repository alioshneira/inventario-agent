from django.contrib import admin
from .models import Server, Device, Mount

# Register your models here.
admin.site.register(Server)
admin.site.register(Device)
admin.site.register(Mount)
