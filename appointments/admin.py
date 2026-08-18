from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = (
        "patient",
        "dentist",
        "service",
        "appointment_date",
        "appointment_time",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "dentist",
        "service",
        "appointment_date",
    )

    search_fields = (
        "patient__full_name",
        "patient__phone",
        "patient__email",
        "dentist__name",
        "service__name",
    )

    ordering = (
        "-appointment_date",
        "-appointment_time",
    )

    list_per_page = 20