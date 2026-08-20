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
    )

    search_fields = (
        "patient__full_name",
        "patient__phone",
        "dentist__name",
        "service__name",
    )

    list_filter = (
        "status",
        "dentist",
        "service",
        "appointment_date",
    )

    date_hierarchy = "appointment_date"

    list_editable = (
        "status",
    )

    ordering = (
        "appointment_date",
        "appointment_time",
    )