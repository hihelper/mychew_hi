from django.contrib import admin
from .models import BlogUser

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'phonenumber', 'register_date',)


admin.site.register(BlogUser, UserAdmin)
