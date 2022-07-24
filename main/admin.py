from django.contrib import admin
from .models import *


class Admin(admin.ModelAdmin):
    pass


admin.site.register(Email, Admin)
admin.site.register(User, Admin)