from django.contrib import admin
from django.urls import path, include

from clinic.views import home


urlpatterns = [

    path(
        "admin/",
        admin.site.urls,
    ),

    path(
        "",
        home,
        name="home",
    ),

    path(
        "appointments/",
        include("appointments.urls"),
    ),

]