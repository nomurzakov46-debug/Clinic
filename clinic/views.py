from django.shortcuts import render,get_object_or_404,redirect
from .models import Direction,Doctor
from pages.models import Review
from .forms import AppointmentForm,CallRequestForm,OmsRequestForm
from django.core.paginator import Paginator

def direction_list(request):
    directions = Direction.objects.all()
    return render(request,'directions.html',{'directions':directions})


def direction_detail(request,slug):
    direction = get_object_or_404(Direction,slug=slug)
    reviews = Review.objects.filter(is_approved=True,doctor__direction=direction)[:2]
    return render(request,'direction_detail.html',{'direction':direction,'reviews':reviews})

def doctor_list(request):
    doctors = Doctor.objects.all()
    paginator = Paginator(doctors,12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'doctors.html',{'page_obj':page_obj})

def doctor_detail(request,pk):
    doctor = get_object_or_404(Doctor,pk=pk)
    return render(request,'doctor_detail.html',{'doctor':doctor})

def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'appointment.html',{'success':True})
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})


def callback_create(request):
    if request.method == 'POST':
        form = CallRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER','home'))
        
    return redirect('home')



