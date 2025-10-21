from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import Admin, Doctor, Patient
from django.contrib.auth import authenticate, login
from django.urls import reverse

#dashboard view
def dashboard(request):
    return render(request, 'dashboard.html')

# User Login View
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)

            # Check if the user is a Doctor, Patient, or Admin and redirect accordingly
            if hasattr(user, 'doctor'):
                return redirect('hospital:doctor_dashboard')  # Updated with namespaced URL
            elif hasattr(user, 'patient'):
                return redirect('hospital:patient_dashboard')  # Updated with namespaced URL
            elif hasattr(user, 'admin'):  # For admin users (Django superuser check)
                return redirect(('hospital:admin_dashboard'))  # Namespaced redirect
            else:
                messages.error(request, "Unauthorized user type!")
                return redirect('login')  # Redirect to login if user type is unknown
        else:
            messages.error(request, "Invalid username or password!")
    
    return render(request, 'login.html')

# Admin Registration View
def register_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        contact_number = request.POST.get('contact_number')
        address = request.POST.get('address')

        if username and email and password:
            user = User(username=username, email=email, password=make_password(password))
            user.save()

            admin = Admin(
                user=user,
                first_name=first_name,
                last_name=last_name,
                contact_number=contact_number,
                address=address,
            )
            admin.save()

            messages.success(request, "Admin registered successfully!")
            return redirect('login')
        else:
            messages.error(request, "Please fill all required fields!")

    return render(request, 'register_admin.html')


# Doctor Registration View
def register_doctor(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        specialization = request.POST.get('specialization')
        contact_number = request.POST.get('contact_number')
        experience_years = request.POST.get('experience_years')
        available_days = request.POST.get('available_days')

        if username and email and password:
            user = User(username=username, email=email, password=make_password(password))
            user.save()

            doctor = Doctor(
                user=user,
                first_name=first_name,
                last_name=last_name,
                specialization=specialization,
                contact_number=contact_number,
                experience_years=experience_years,
                available_days=available_days,
            )
            doctor.save()

            messages.success(request, "Doctor registered successfully!")
            return redirect('login')
        else:
            messages.error(request, "Please fill all required fields!")

    return render(request, 'register_doctor.html')


# Patient Registration View
def register_patient(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        contact_number = request.POST.get('contact_number')

        if username and email and password:
            user = User(username=username, email=email, password=make_password(password))
            user.save()

            patient = Patient(
                user=user,
                first_name=first_name,
                last_name=last_name,
                age=age,
                address=address,
                contact_number=contact_number,
            )
            patient.save()

            messages.success(request, "Patient registered successfully!")
            return redirect('login')
        else:
            messages.error(request, "Please fill all required fields!")

    return render(request, 'register_patient.html')
