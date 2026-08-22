from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Email address or Phone number",
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Enter Email or Phone number",
                "autofocus": True,
            }
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-input",
                "placeholder": "Password",
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update(
                {"class": "form-input", "style": "width: 100%; box-sizing: border-box;"}
            )


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-input", "placeholder": "First Name"}
        ),
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-input", "placeholder": "Last Name"}
        ),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "form-input", "placeholder": "Email Address"}
        ),
    )
    phone = forms.CharField(
        required=True,
        max_length=20,
        widget=forms.TextInput(
            attrs={"class": "form-input", "placeholder": "+880 1XXXXXXXXX"}
        ),
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "phone")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply full-width styling to all fields including password1 & password2
        for field in self.fields.values():
            field.widget.attrs.update(
                {"class": "form-input", "style": "width: 100%; box-sizing: border-box;"}
            )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            from clinic.models import Patient
            Patient.objects.update_or_create(
                email=user.email,
                defaults={
                    "full_name": f"{user.first_name} {user.last_name}".strip(),
                    "phone": self.cleaned_data["phone"],
                },
            )
        return user