from django.contrib import messages
from django.shortcuts import redirect, render

from appointments.models import Appointment
from .forms import GalleryImageForm
from .models import Dentist, GalleryImage, Patient, Service

# clinic/views.py
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required(login_url='login')
def dashboard(request):
    # Your existing dashboard logic...
    ...


def home(request):
    dentists = Dentist.objects.all()
    services = Service.objects.filter(is_active=True)
    gallery_images = GalleryImage.objects.filter(is_active=True)[:6]

    context = {
        "dentists": dentists,
        "services": services,
        "gallery_images": gallery_images,
    }

    return render(request, "home.html", context)


def upload_gallery_image(request):
    if request.method == "POST":
        form = GalleryImageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Gallery photo uploaded successfully!")
            return redirect("home")
    else:
        form = GalleryImageForm()

    return render(request, "clinic/upload_gallery.html", {"form": form})


def dashboard(request):
    total_patients = Patient.objects.count()
    total_dentists = Dentist.objects.count()
    total_services = Service.objects.filter(is_active=True).count()
    total_appointments = Appointment.objects.count()

    pending_appointments = Appointment.objects.filter(status="pending").count()
    confirmed_appointments = Appointment.objects.filter(status="confirmed").count()
    completed_appointments = Appointment.objects.filter(status="completed").count()
    cancelled_appointments = Appointment.objects.filter(status="cancelled").count()

    recent_appointments = (
        Appointment.objects.select_related("patient", "dentist", "service")
        .order_by("-created_at")[:5]
    )

    upcoming_appointments = (
        Appointment.objects.select_related("patient", "dentist", "service")
        .filter(status__in=["pending", "confirmed"])
        .order_by("appointment_date", "appointment_time")[:5]
    )

    context = {
        "total_patients": total_patients,
        "total_dentists": total_dentists,
        "total_services": total_services,
        "total_appointments": total_appointments,
        "pending_appointments": pending_appointments,
        "confirmed_appointments": confirmed_appointments,
        "completed_appointments": completed_appointments,
        "cancelled_appointments": cancelled_appointments,
        "recent_appointments": recent_appointments,
        "upcoming_appointments": upcoming_appointments,
    }

    return render(request, "dashboard.html", context)