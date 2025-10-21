from django.contrib import admin
from .models import Appointment  # Import Appointment model


# Customize Appointment Admin Display
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment_date', 'appointment_time', 'status')
    list_filter = ('status', 'appointment_date')
    search_fields = ('patient__user__username', 'doctor__user__username', 'symptoms')
    ordering = ('appointment_date', 'appointment_time')

admin.site.register(Appointment, AppointmentAdmin)