from django.shortcuts import render
from .models import Dentist, Service


def home(request):
    dentists = Dentist.objects.all()
    services = Service.objects.filter(is_active=True)

    context = {
        "dentists": dentists,
        "services": services,
    }

    return render(request, "home.html", context)