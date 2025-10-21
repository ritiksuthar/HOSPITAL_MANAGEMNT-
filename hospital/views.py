from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from .models import Appointment 
from accounts.models import Doctor

# Admin Dashboard View
@login_required
def AdminDashboard(request):
    if hasattr(request.user, 'admin'):
        return render(request, 'admin/admin_dashboard.html')
    else:
        messages.error(request, "Access denied. You are not authorized to view this page.")
        return redirect('login')

# Patient Dashboard View
@login_required
def PatientDashboard(request):
    if hasattr(request.user, 'patient'):
        return render(request, 'patient/patient_dashboard.html')
    else:
        messages.error(request, "Access denied. You are not authorized to view this page.")
        return redirect('login')

# Doctor Dashboard View
@login_required
def DoctorDashboard(request):
    if hasattr(request.user, 'doctor'):
        doctor = Doctor.objects.get(user=request.user)# Assume the user is a doctor

        # Fetching appointment stats
        total_appointments = Appointment.objects.filter(doctor=doctor).count()
        pending_appointments = Appointment.objects.filter(doctor=doctor, status='Pending').count()
        completed_appointments = Appointment.objects.filter(doctor=doctor, status='Completed').count()

        # Fetching recent appointments (latest 5)
        recent_appointments = Appointment.objects.filter(doctor=doctor).order_by('-appointment_date')[:5]

        context = {
            'total_appointments': total_appointments,
            'pending_appointments': pending_appointments,
            'completed_appointments': completed_appointments,
            'recent_appointments': recent_appointments,
        }

        return render(request, 'doctor/doctor_dashboard.html', context)
    else:
        messages.error(request, "Access denied. You are not authorized to view this page.")
        return redirect('login')
    

# Appointment List View
@login_required
def AppointmentList(request):
    if hasattr(request.user, 'doctor'):
        appointments = Appointment.objects.all()
        return render(request, 'doctor/view_appointments.html', {'appointments': appointments})
    else:
        messages.error(request, "Access denied. You are not authorized to view this page.")
        return redirect('login')
    
# Patient Records View
@login_required
def PatientRecords(request):
    if hasattr(request.user, 'doctor'):
        return render(request, 'doctor/patient_records.html')
    else:
        messages.error(request, "Access denied. You are not authorized to view this page.")
        return redirect('login')
    
# Book Appointment 
from django.utils.timezone import now
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Appointment, Doctor, Patient

@login_required
def book_appointment(request):
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()  # Fetch patients if needed
    
    if request.method == "POST":
        patient_id = request.POST.get('patient')  # Fetch patient ID
        doctor_id = request.POST.get('doctor')    # Fetch doctor ID
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        symptoms = request.POST.get('symptoms')  # Save message as symptoms


        if not patient_id or not doctor_id or not appointment_date or not appointment_time:
            return HttpResponse("Error: Missing required fields.", status=400)  # Debugging ke liye

        try:
            appointment_date = datetime.strptime(appointment_date, "%Y-%m-%d").date()
            appointment_time = datetime.strptime(appointment_time, "%H:%M").time()
        except ValueError:
            return HttpResponse("Invalid date or time format", status=400)


        # Get patient and doctor objects
        patient = get_object_or_404(Patient, id=patient_id)
        doctor = get_object_or_404(Doctor, id=doctor_id)
       
        # Create and save appointment
        appointment = Appointment(
            patient=patient,
            doctor=doctor,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            symptoms=symptoms
        )
        
        appointment.save()
        
        
        messages.success(request, "Your appointment has been successfully booked!")
        return render(request, 'admin/book_appointment.html', {'doctors': doctors, 'patients': patients})
 
    return render(request, 'admin/book_appointment.html', {'doctors': doctors, 'patients': patients})


#appointment list 
@login_required
def view_appointments(request):
    if hasattr(request.user, 'admin'):
        appointments = Appointment.objects.all()
        return render(request, 'doctor/view_appointments.html', {'appointments': appointments})
    else:
        messages.error(request, "Access denied. You are not authorized to view this page.")
        return redirect('login')