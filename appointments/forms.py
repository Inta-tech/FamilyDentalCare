from django import forms
from clinic.models import Patient, Dentist, Service
from .models import Appointment


class AppointmentForm(forms.Form):

    # -----------------------------
    # Patient Information
    # -----------------------------

    full_name = forms.CharField(
        max_length=150,
        label="Full Name",
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Enter your full name",
            }
        ),
    )

    phone = forms.CharField(
        max_length=20,
        label="Phone Number",
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "+880 1XXXXXXXXX",
            }
        ),
    )

    email = forms.EmailField(
        required=False,
        label="Email Address",
        widget=forms.EmailInput(
            attrs={
                "class": "form-input",
                "placeholder": "your@email.com",
            }
        ),
    )

    date_of_birth = forms.DateField(
        required=False,
        label="Date of Birth",
        widget=forms.DateInput(
            attrs={
                "class": "form-input",
                "type": "date",
            }
        ),
    )

    gender = forms.ChoiceField(
        required=False,
        label="Gender",
        choices=[
            ("", "Select gender"),
            ("Male", "Male"),
            ("Female", "Female"),
            ("Other", "Other"),
        ],
        widget=forms.Select(
            attrs={
                "class": "form-input",
            }
        ),
    )

    address = forms.CharField(
        required=False,
        label="Address",
        widget=forms.Textarea(
            attrs={
                "class": "form-input",
                "placeholder": "Enter your address",
                "rows": 3,
            }
        ),
    )

    emergency_contact = forms.CharField(
        required=False,
        max_length=20,
        label="Emergency Contact",
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Emergency contact number",
            }
        ),
    )

    # -----------------------------
    # Appointment Information
    # -----------------------------

    dentist = forms.ModelChoiceField(
        queryset=Dentist.objects.all(),
        empty_label="Select a dentist",
        label="Preferred Dentist",
        widget=forms.Select(
            attrs={
                "class": "form-input",
            }
        ),
    )

    service = forms.ModelChoiceField(
        queryset=Service.objects.filter(is_active=True),
        empty_label="Select a dental service",
        label="Dental Service",
        widget=forms.Select(
            attrs={
                "class": "form-input",
            }
        ),
    )

    appointment_date = forms.DateField(
        label="Preferred Date",
        widget=forms.DateInput(
            attrs={
                "class": "form-input",
                "type": "date",
            }
        ),
    )

    appointment_time = forms.TimeField(
        label="Preferred Time",
        widget=forms.TimeInput(
            attrs={
                "class": "form-input",
                "type": "time",
            }
        ),
    )

    reason = forms.CharField(
        required=False,
        label="Reason for Visit",
        widget=forms.Textarea(
            attrs={
                "class": "form-input",
                "placeholder": "Tell us briefly why you need an appointment",
                "rows": 4,
            }
        ),
    )

    notes = forms.CharField(
        required=False,
        label="Additional Notes",
        widget=forms.Textarea(
            attrs={
                "class": "form-input",
                "placeholder": "Anything else we should know?",
                "rows": 4,
            }
        ),
    )

    def clean_phone(self):
        phone = self.cleaned_data["phone"].strip()

        if len(phone) < 8:
            raise forms.ValidationError(
                "Please enter a valid phone number."
            )

        return phone

    def clean(self):
        cleaned_data = super().clean()

        appointment_date = cleaned_data.get("appointment_date")
        appointment_time = cleaned_data.get("appointment_time")

        if appointment_date and appointment_time:

            from django.utils import timezone

            appointment_datetime = timezone.make_aware(
                timezone.datetime.combine(
                    appointment_date,
                    appointment_time,
                )
            )

            if appointment_datetime < timezone.now():
                raise forms.ValidationError(
                    "Please select a future date and time."
                )

        return cleaned_data