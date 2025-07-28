from django.db import models


class Type(models.Model):
    """Type of cash flow operation."""

    name = models.CharField(max_length=50, unique=True, verbose_name="Тип")

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"

    def __str__(self) -> str:
        return self.name
