from typing import Any

from django import forms

from cashflow.models import Operation


class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = [
            "created_at",
            "status",
            "type",
            "category",
            "subcategory",
            "amount",
            "comment",
        ]

    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        type_ = cleaned_data.get("type")
        category = cleaned_data.get("category")
        subcategory = cleaned_data.get("subcategory")

        if category.type != type_:
            self.add_error(
                "category",
                "Выбранная категория не связана с текущем типом операции.",
            )

        if subcategory.category != category:
            self.add_error(
                "subcategory",
                "Выбранная подкатегория не связана с текущей категорией.",
            )

        return cleaned_data
