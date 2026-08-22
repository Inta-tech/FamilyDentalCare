from django.db import models

from clinic.models import Patient, Dentist, Service


class Appointment(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
        ("no_show", "No Show"),
    ]

    patient = models.ForeignKey(
        Patient,
        on_delete=models.PROTECT,
        related_name="appointments",
    )

    dentist = models.ForeignKey(
        Dentist,
        on_delete=models.PROTECT,
        related_name="appointments",
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.PROTECT,
        related_name="appointments",
    )

    appointment_date = models.DateField()

    appointment_time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
    )

    reason = models.TextField(blank=True)

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = [
            "-appointment_date",
            "-appointment_time",
        ]

    def __str__(self):
        return (
            f"{self.patient.full_name} - "
            f"{self.appointment_date} "
            f"{self.appointment_time}"
        )