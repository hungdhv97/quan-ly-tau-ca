from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "created_at",
        "updated_at",
    )
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("is_active",)
