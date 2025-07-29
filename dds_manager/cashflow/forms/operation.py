from django import forms

from cashflow.models import Operation


class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        type_ = cleaned_data.get("type")
        category = cleaned_data.get("category")
        subcategory = cleaned_data.get("subcategory")

        if category.type != type_:
            self.add_error(
                "category", "Выбранная категория не связана с текущем типом операции."
            )

        if subcategory.category != category:
            self.add_error(
                "subcategory", "Выбранная подкатегория не связана с текущей категорией."
            )
