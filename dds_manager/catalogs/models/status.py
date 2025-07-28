from django.db import models


class Status(models.Model):
    """Model for cash flow statuses."""

    name = models.CharField(max_length=50, unique=True, verbose_name="Статус")

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self) -> str:
        return self.name
