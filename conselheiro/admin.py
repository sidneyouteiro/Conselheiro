from django.contrib import admin

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import *
from .models import *


class CustomUserAdmin(UserAdmin):
    add_form = FormRegistro
    form = FormTrocaPeriodo
    model = User
    list_display = ['username', 'periodo']


admin.site.register(User, UserAdmin)
admin.site.register(Tracking)