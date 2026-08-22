from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import AppointmentForm, create_appointment


def book_appointment(request, dentist_id=None):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            create_appointment(form)
            messages.success(
                request,
                "Appointment booked successfully! We look forward to seeing you.",
            )
            return redirect("home")
    else:
        initial_data = {}

        # Auto-fill user information if logged in
        if request.user.is_authenticated:
            full_name = (
                f"{request.user.first_name} {request.user.last_name}".strip()
            )
            initial_data["full_name"] = (
                full_name if full_name else request.user.username
            )
            initial_data["email"] = request.user.email

        # Pre-select dentist passed via path variable or URL parameter (?dentist=ID)
        selected_dentist = dentist_id or request.GET.get("dentist")
        if selected_dentist:
            initial_data["dentist"] = selected_dentist

        # Pre-select service passed via URL parameter (?service=ID)
        service_id = request.GET.get("service")
        if service_id:
            initial_data["service"] = service_id

        form = AppointmentForm(initial=initial_data)

    return render(request, "appointments/book.html", {"form": form})