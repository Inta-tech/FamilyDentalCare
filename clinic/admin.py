from django.contrib import admin
from .models import ClinicSetting

@admin.register(ClinicSetting)
class ClinicSettingAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email")

    def has_add_permission(self, request):
        # Prevent creating multiple settings instances
        if ClinicSetting.objects.exists():
            return False
        return super().has_add_permission(request)


from .models import (
    Patient,
    Dentist,
    Service,
    Treatment,
    TreatmentImage,
    GalleryImage,
)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "phone",
        "email",
        "gender",
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

    date_hierarchy = "created_at"


@admin.register(Dentist)
class DentistAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "specialization",
        "qualification",
        "experience",
        "phone",
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

    search_fields = (
        "name",
        "description",
    )

    list_filter = (
        "is_active",
    )


@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):

    list_display = (
        "patient",
        "dentist",
        "service",
        "treatment_date",
    )

    search_fields = (
        "patient__full_name",
        "dentist__name",
        "service__name",
    )

    list_filter = (
        "service",
        "dentist",
        "treatment_date",
    )

    date_hierarchy = "treatment_date"


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


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "is_active",
        "created_at",
    )

    search_fields = (
        "title",
        "caption",
    )

    list_filter = (
        "category",
        "is_active",
        "created_at",
    )

    date_hierarchy = "created_at"