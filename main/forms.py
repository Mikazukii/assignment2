from django.forms import ModelForm
from main.models import ProductEntry
from django.utils.html import strip_tags
from django import forms


class ProductEntryForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields = ["product", "feedback", "note"]
        widgets = {
            "field1": forms.TextInput(
                attrs={
                    "class": "border border-red-300 focus:ring-red-500 focus:border-red-500 block w-full rounded-md shadow-sm"
                }
            ),
            "field2": forms.TextInput(
                attrs={
                    "class": "border border-red-300 focus:ring-red-500 focus:border-red-500 block w-full rounded-md shadow-sm"
                }
            ),
        }

    def clean_mood(self):
        product = self.cleaned_data["product"]
        return strip_tags(product)

    def clean_feelings(self):
        note = self.cleaned_data["note"]
        return strip_tags(note)
