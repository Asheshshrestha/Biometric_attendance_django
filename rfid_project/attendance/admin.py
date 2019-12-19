from django.contrib import admin
from .models import User, Log,Mode_Type

# Register your models here.

admin.site.register(User)
admin.site.register(Log)
admin.site.register(Mode_Type)