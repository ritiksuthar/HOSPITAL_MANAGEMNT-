from django.contrib import admin
from .models import Patient, Doctor, Admin

# Patient Admin Panel
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'age', 'contact_number', 'date_registered')
    search_fields = ('first_name', 'last_name', 'email', 'contact_number')
    list_filter = ('date_registered',)


# Doctor Admin Panel
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'specialization', 'experience_years', 'contact_number')
    search_fields = ('first_name', 'last_name', 'email', 'specialization', 'contact_number')
    list_filter = ('specialization',)


# Admin Panel for Admin Model
@admin.register(Admin)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'contact_number', 'address')
    search_fields = ('first_name', 'last_name', 'email', 'contact_number')
