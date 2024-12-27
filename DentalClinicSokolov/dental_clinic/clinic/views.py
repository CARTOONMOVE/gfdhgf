from django.shortcuts import render, redirect
from .models import Service, Appointment
from .forms import AppointmentForm

def home(request):
    return render(request, 'clinic/home.html', {})

def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AppointmentForm()
    return render(request, 'clinic/book_appointment.html', {'form': form})