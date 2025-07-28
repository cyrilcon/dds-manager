from django.db import models


class Category(models.Model):
    """Category linked to a specific type."""

    name = models.CharField(max_length=100, unique=True, verbose_name="Категория")
    type = models.ForeignKey(
        "Type",
        on_delete=models.CASCADE,
        related_name="categories",
        verbose_name="Тип",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.name
