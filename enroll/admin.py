from django.contrib.admin.sites import site
from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    user_data = ('name', 'email', 'password')


site.register(User, UserAdmin)

# Register your models here.
