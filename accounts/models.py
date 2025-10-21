from django.db import models
from django.contrib.auth.models import User

# Patient Model
class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


# Doctor Model
class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    experience_years = models.PositiveIntegerField()
    available_days = models.CharField(max_length=100, help_text="E.g., Mon, Wed, Fri")

    def __str__(self):
        return f"Dr. {self.user.username} - {self.specialization}"


class Admin(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    

    def __str__(self):
        return self.user.username
