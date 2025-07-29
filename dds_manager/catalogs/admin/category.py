from django.contrib import admin

from catalogs.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "type"]
    list_filter = ["type__name"]
    search_fields = ["name", "type__name"]
