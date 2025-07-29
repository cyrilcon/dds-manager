from django.contrib import admin
from django.contrib.auth.models import Group, User
from rangefilter.filters import DateRangeQuickSelectListFilter

from cashflow.models import Operation


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    fields = [
        "created_at",
        "status",
        "type",
        "category",
        "subcategory",
        "amount",
        "comment",
    ]
    list_display = [
        "created_at",
        "status",
        "type",
        "category",
        "subcategory",
        "amount_rubles",
        "comment",
    ]
    list_filter = [
        ("created_at", DateRangeQuickSelectListFilter),
        "status",
        "type",
        "category",
        "subcategory",
    ]
    search_fields = [
        "status__name",
        "type__name",
        "category__name",
        "subcategory__name",
    ]
    date_hierarchy = "created_at"

    @admin.display(description="Сумма", ordering="amount")
    def amount_rubles(self, operation: Operation) -> str:
        return f"{operation.amount:,.2f}₽"


admin.site.site_header = "ДДС Менеджер"
admin.site.index_title = "Администрирование ДДС"
admin.site.site_title = "ДДС Менеджер"

# Disable "Users and Groups" from the admin panel
admin.site.unregister(User)
admin.site.unregister(Group)
