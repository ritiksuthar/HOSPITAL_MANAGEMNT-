from django.urls import path
from . import views
app_name = 'hospital'  # Add namespace for hospital app
urlpatterns = [
    path('admin_dashboard', views.AdminDashboard, name='admin_dashboard'),
    path('doctor_dashboard/', views.DoctorDashboard, name='doctor_dashboard'),
    path('patient_dashboard/', views.PatientDashboard, name='patient_dashboard'),
    path('appointment_list/', views.AppointmentList, name='view_appointments'),
    path('patient_records/', views.PatientRecords, name='patient_records'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('view_appointments/', views.view_appointments, name='view_appointments'),
]
