from django.contrib import admin

from catalogs.models import Type


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
