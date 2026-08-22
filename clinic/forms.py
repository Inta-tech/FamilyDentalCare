from django import forms
from .models import GalleryImage


class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ["title", "category", "image", "caption", "is_active"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Event or Procedure Title",
                }
            ),
            "category": forms.Select(attrs={"class": "form-input"}),
            "image": forms.FileInput(
                attrs={"class": "form-input", "accept": "image/*"}
            ),
            "caption": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Short description",
                }
            ),
            "is_active": forms.CheckboxInput(
                attrs={"class": "form-checkbox"}
            ),
        }