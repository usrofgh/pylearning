from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from catalog.models import Author, LiteraryFormat, Book


@admin.register(Author)
class AuthorAdmin(UserAdmin):
    list_display = ["username", "first_name", "last_name", "email", "is_active", "is_superuser"]
    list_filter = ["is_active", "is_superuser"]
    search_fields = ["username", "email"]

    fieldsets = (
        ("Additional info",
         {"fields": ("username", "email", "first_name", "last_name", "is_superuser")}
         ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info",
         {"fields": ("first_name", "last_name")}
         ),
    )


@admin.register(LiteraryFormat)
class LiteraryFormatAdmin(admin.ModelAdmin):
    search_fields = ["name"]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "format"]
    list_filter = ["format"]
    search_fields = ["title", "price"]
