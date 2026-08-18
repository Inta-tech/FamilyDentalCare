from django.db import models


class Patient(models.Model):
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    emergency_contact = models.CharField(max_length=20, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.full_name


class Dentist(models.Model):
    name = models.CharField(max_length=150)
    specialization = models.CharField(max_length=150)
    qualification = models.CharField(max_length=200, blank=True)
    experience = models.PositiveIntegerField(default=0)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    profile_photo = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image_url = models.URLField(blank=True)
    starting_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    duration_minutes = models.PositiveIntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Treatment(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.PROTECT,
        related_name="treatments"
    )
    dentist = models.ForeignKey(
        Dentist,
        on_delete=models.PROTECT,
        related_name="treatments"
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.PROTECT,
        related_name="treatments"
    )
    treatment_date = models.DateField()
    description = models.TextField()
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-treatment_date"]

    def __str__(self):
        return f"{self.patient.full_name} - {self.service.name}"


class TreatmentImage(models.Model):
    IMAGE_TYPES = [
        ("before", "Before"),
        ("after", "After"),
        ("during", "During"),
        ("other", "Other"),
    ]

    treatment = models.ForeignKey(
        Treatment,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image_url = models.URLField()
    image_type = models.CharField(
        max_length=20,
        choices=IMAGE_TYPES
    )
    caption = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.treatment} - {self.image_type}"