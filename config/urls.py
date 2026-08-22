from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("clinic.urls")),
    path("appointments/", include("appointments.urls")),
    path("accounts/", include("accounts.urls")),  # This correctly routes login & logout
]