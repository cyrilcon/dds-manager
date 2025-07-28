from django.db import models


class Operation(models.Model):
    """Record of cash flow."""

    created_at = models.DateField(
        verbose_name="Дата создания записи",
        auto_now_add=True,
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
    category = models.ForeignKey(
        "catalogs.Category",
        on_delete=models.PROTECT,
        verbose_name="Категория",
        related_name="operations",
    )
    subcategory = models.ForeignKey(
        "catalogs.Subcategory",
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
        verbose_name = "Запись о движении денежных средств"
        verbose_name_plural = "Записи о движении денежных средств"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.created_at} | {self.status} | {self.type} | {self.category} | {self.subcategory} | {self.amount}₽"
