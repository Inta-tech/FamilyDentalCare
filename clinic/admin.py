from django.contrib import admin
from .models import Patient, Dentist, Service, Treatment, TreatmentImage


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "phone",
        "email",
        "gender",
        "date_of_birth",
        "created_at",
    )

    search_fields = (
        "full_name",
        "phone",
        "email",
    )

    list_filter = (
        "gender",
        "created_at",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 20

@admin.register(Dentist)
class DentistAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "specialization",
        "qualification",
        "experience",
    )

    search_fields = (
        "name",
        "specialization",
        "qualification",
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "starting_price",
        "duration_minutes",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "description",
    )


@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):

    list_display = (
        "patient",
        "dentist",
        "service",
        "treatment_date",
    )

    list_filter = (
        "service",
        "dentist",
        "treatment_date",
    )

    search_fields = (
        "patient__full_name",
        "dentist__name",
        "service__name",
    )


@admin.register(TreatmentImage)
class TreatmentImageAdmin(admin.ModelAdmin):

    list_display = (
        "treatment",
        "image_type",
        "caption",
        "created_at",
    )

    list_filter = (
        "image_type",
    )