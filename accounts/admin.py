from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'contact_no', 'is_active', 'is_staff', 'date_joined', 'created_at')
    list_filter = ('is_active', 'is_staff', 'date_joined', 'created_at')
    search_fields = ('email', 'first_name', 'last_name', 'contact_no')
    ordering = ('-created_at',)


