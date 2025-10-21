from django.db import models
from accounts.models import Doctor, Patient  # Importing models from another app
from django.utils.timezone import now

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField(default=now)
    appointment_time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    symptoms = models.TextField(blank=True)

    def __str__(self):
        return f"Appointment: {self.patient} with {self.doctor} on {self.appointment_date} at {self.appointment_time}"
