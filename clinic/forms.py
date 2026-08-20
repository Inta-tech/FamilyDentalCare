from django import forms
from .models import GalleryImage


class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ["title", "category", "image_url", "caption", "is_active"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Event or Procedure Title"}
            ),
            "category": forms.Select(attrs={"class": "form-input"}),
            "image_url": forms.URLInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "https://r2.cloudflare.com/.../photo.jpg",
                }
            ),
            "caption": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Short description"}
            ),
            "is_active": forms.CheckboxInput(),
        }