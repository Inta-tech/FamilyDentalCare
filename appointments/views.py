from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction

from clinic.models import Patient

from .forms import AppointmentForm
from .models import Appointment


def book_appointment(request):

    if request.method == "POST":

        form = AppointmentForm(request.POST)

        if form.is_valid():

            with transaction.atomic():

                patient, created = Patient.objects.get_or_create(
                    phone=form.cleaned_data["phone"],
                    defaults={
                        "full_name": form.cleaned_data["full_name"],
                        "email": form.cleaned_data["email"],
                        "date_of_birth": form.cleaned_data["date_of_birth"],
                        "gender": form.cleaned_data["gender"],
                        "address": form.cleaned_data["address"],
                        "emergency_contact": form.cleaned_data[
                            "emergency_contact"
                        ],
                    },
                )

                if not created:

                    patient.full_name = form.cleaned_data["full_name"]
                    patient.email = form.cleaned_data["email"]
                    patient.date_of_birth = form.cleaned_data[
                        "date_of_birth"
                    ]
                    patient.gender = form.cleaned_data["gender"]
                    patient.address = form.cleaned_data["address"]
                    patient.emergency_contact = form.cleaned_data[
                        "emergency_contact"
                    ]

                    patient.save()

                Appointment.objects.create(
                    patient=patient,
                    dentist=form.cleaned_data["dentist"],
                    service=form.cleaned_data["service"],
                    appointment_date=form.cleaned_data[
                        "appointment_date"
                    ],
                    appointment_time=form.cleaned_data[
                        "appointment_time"
                    ],
                    reason=form.cleaned_data["reason"],
                    notes=form.cleaned_data["notes"],
                    status="pending",
                )

            messages.success(
                request,
                "Your appointment request has been submitted successfully. "
                "Our team will contact you to confirm the appointment.",
            )

            return redirect("appointments:book")

    else:

        form = AppointmentForm()

    return render(
        request,
        "appointments/book.html",
        {
            "form": form,
        },
    )