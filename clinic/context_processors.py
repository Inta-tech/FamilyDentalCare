from .models import ClinicSetting

def clinic_settings(request):
    settings = ClinicSetting.objects.first()
    if not settings:
        settings = ClinicSetting.objects.create(name="Family Dental Care")
    return {"clinic_settings": settings}