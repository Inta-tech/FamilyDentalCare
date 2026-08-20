from django.urls import path

from .views import dashboard, home, upload_gallery_image

urlpatterns = [
    path(
        "",
        home,
        name="home",
    ),
    path(
        "dashboard/",
        dashboard,
        name="dashboard",
    ),
    path(
        "gallery/upload/",
        upload_gallery_image,
        name="upload_gallery_image",
    ),
]