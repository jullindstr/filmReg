from django.contrib import admin

from .models import Users, Films

admin.site.register(Users)
admin.site.register(Films)