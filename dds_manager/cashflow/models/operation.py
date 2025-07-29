from django.db import models
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey


class Operation(models.Model):
    """Record of cash flow."""

    created_at = models.DateField(
        verbose_name="Дата создания записи",
        default=timezone.now,
        help_text="Заполняется автоматически, но может быть изменена вручную",
    )
    status = models.ForeignKey(
        "catalogs.Status",
        on_delete=models.PROTECT,
        verbose_name="Статус",
        related_name="operations",
    )
    type = models.ForeignKey(
        "catalogs.Type",
        on_delete=models.PROTECT,
        verbose_name="Тип",
        related_name="operations",
    )
    category = ChainedForeignKey(
        "catalogs.Category",
        chained_field="type",
        chained_model_field="type",
        show_all=False,
        auto_choose=False,
        sort=True,
        on_delete=models.PROTECT,
        verbose_name="Категория",
        related_name="operations",
    )
    subcategory = ChainedForeignKey(
        "catalogs.Subcategory",
        chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=False,
        sort=True,
        on_delete=models.PROTECT,
        verbose_name="Подкатегория",
        related_name="operations",
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Сумма",
        help_text="Сумма в рублях.",
    )
    comment = models.TextField(
        blank=True,
        verbose_name="Комментарий",
        help_text="Необязательное поле",
    )

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.created_at.strftime("%d.%m.%Y")} | {self.status} | {self.type} | {self.category} | {self.subcategory} | {self.amount}₽"
