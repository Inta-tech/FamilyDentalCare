from django import forms
from clinic.models import Dentist, Patient, Service
from .models import Appointment


class AppointmentForm(forms.Form):

    booking_for_other = forms.BooleanField(
        required=False,
        label="Booking for someone else?",
        widget=forms.CheckboxInput(
            attrs={
                "id": "id_booking_for_other",
                "onchange": "togglePatientFields()",
            }
        ),
    )

    full_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Enter patient's full name",
                "id": "id_full_name",
            }
        ),
    )

    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "+880 1XXXXXXXXX",
                "id": "id_phone",
            }
        ),
    )

    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={
                "class": "form-input",
                "placeholder": "patient@example.com",
                "id": "id_email",
            }
        ),
    )

    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                "class": "form-input",
                "type": "date",
                "id": "id_date_of_birth",
            }
        ),
    )

    gender = forms.CharField(
        required=False,
        widget=forms.Select(
            choices=[
                ("", "Select gender"),
                ("Male", "Male"),
                ("Female", "Female"),
                ("Other", "Other"),
            ],
            attrs={
                "class": "form-input",
                "id": "id_gender",
            },
        ),
    )

    emergency_contact = forms.CharField(
        required=False,
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Emergency contact number",
                "id": "id_emergency_contact",
            }
        ),
    )

    address = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-input",
                "placeholder": "Patient address",
                "rows": 3,
                "id": "id_address",
            }
        ),
    )

    dentist = forms.ModelChoiceField(
        queryset=Dentist.objects.all(),
        empty_label="Select dentist",
        widget=forms.Select(
            attrs={
                "class": "form-input",
            }
        ),
    )

    service = forms.ModelChoiceField(
        queryset=Service.objects.filter(is_active=True),
        empty_label="Select dental service",
        widget=forms.Select(
            attrs={
                "class": "form-input",
            }
        ),
    )

    appointment_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "class": "form-input",
                "type": "date",
            }
        ),
    )

    appointment_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                "class": "form-input",
                "type": "time",
            }
        ),
    )

    reason = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-input",
                "placeholder": "Reason for your visit",
                "rows": 3,
            }
        ),
    )

    notes = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-input",
                "placeholder": "Any additional information",
                "rows": 3,
            }
        ),
    )


def create_appointment(form):
    patient, created = Patient.objects.get_or_create(
        phone=form.cleaned_data["phone"],
        defaults={
            "full_name": form.cleaned_data["full_name"],
            "email": form.cleaned_data["email"],
            "date_of_birth": form.cleaned_data["date_of_birth"],
            "gender": form.cleaned_data["gender"],
            "address": form.cleaned_data["address"],
            "emergency_contact": form.cleaned_data["emergency_contact"],
        },
    )

    if not created:
        patient.full_name = form.cleaned_data["full_name"]
        patient.email = form.cleaned_data["email"]
        if form.cleaned_data["date_of_birth"]:
            patient.date_of_birth = form.cleaned_data["date_of_birth"]
        if form.cleaned_data["gender"]:
            patient.gender = form.cleaned_data["gender"]
        if form.cleaned_data["address"]:
            patient.address = form.cleaned_data["address"]
        if form.cleaned_data["emergency_contact"]:
            patient.emergency_contact = form.cleaned_data["emergency_contact"]
        patient.save()

    return Appointment.objects.create(
        patient=patient,
        dentist=form.cleaned_data["dentist"],
        service=form.cleaned_data["service"],
        appointment_date=form.cleaned_data["appointment_date"],
        appointment_time=form.cleaned_data["appointment_time"],
        notes=form.cleaned_data["notes"],
    )