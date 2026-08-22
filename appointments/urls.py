from django.urls import path
from .views import book_appointment

urlpatterns = [
    path(
        "book/",
        book_appointment,
        name="book_appointment",
    ),
    path(
        "book/<int:dentist_id>/",
        book_appointment,
        name="book_appointment_with_dentist",
    ),
]