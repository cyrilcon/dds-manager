from django.db import models


class Subcategory(models.Model):
    """Subcategory linked to a category."""

    name = models.CharField(max_length=100, unique=True, verbose_name="Подкатегория")
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="subcategories",
        verbose_name="Категория",
    )

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

    def __str__(self) -> str:
        return self.name
