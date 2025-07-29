from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


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
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.created_at.strftime("%d.%m.%Y")} | {self.status} | {self.type} | {self.category} | {self.subcategory} | {self.amount}₽"

    def clean(self) -> None:
        super().clean()
        if self.category_id and self.category.type_id != self.type_id:
            error_message = "Выбранная категория не относится к выбранному типу."
            raise ValidationError(error_message)

        if self.subcategory_id and self.subcategory.category_id != self.category_id:
            error_message = "Выбранная подкатегория не относится к выбранной категории."
            raise ValidationError(error_message)
