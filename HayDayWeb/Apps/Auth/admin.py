from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]


admin.site.register(User, UserAdmin)