from django.contrib import admin

from catalogs.models import Subcategory


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "category"]
    list_filter = ["category__name"]
    search_fields = ["name", "category__name"]
