from django.shortcuts import render,redirect
from clinic.models import Direction,Doctor,Promotion,Equipment
from clinic.forms import OmsRequestForm
from django.core.paginator import Paginator
from .models import HistoryEvent,Review,ServiceItem

def home(request):
    directions = Direction.objects.all()[:4]
    doctors = Doctor.objects.filter()[:4]
    big_promo = Promotion.objects.filter(is_big=True).order_by('id').first()
    small_promos = Promotion.objects.filter(is_big=False).order_by('id')[:4]
    equipments = Equipment.objects.all()
    return render(request,'home.html',{'directions':directions,'doctors':doctors,'big_promo':big_promo,'small_promos':small_promos,'equipments':equipments})

def patients(request):
    return render(request,'patients.html')

def oms(request):
    return render(request,'oms.html')

def info (request):
    doctors = Doctor.objects.all()
    paginator = Paginator(doctors,12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render (request,'info.html',{'page_obj':page_obj})

def dms(request):
    return render(request,'dms.html')

def contacts(request):
    doctors = Doctor.objects.all()
    print(doctors)
    return render(request,'contacts.html',{'doctors':doctors})


def review_plural(request):
    reviews = Review.objects.filter(is_approved= True,rating=5)[:14]
    return render(request,'review.html',{'reviews':reviews})



def oms(request):
    directions = Direction.objects.all()

    if request.method == 'POST':
        form = OmsRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('oms')
    else:
        form = OmsRequestForm()

    return render(request, 'oms.html', {
        'form': form,
        'directions': directions
    })


def analyses(request):
    promos = Promotion.objects.filter(is_big=True).order_by('id')[:2]
    return render (request,'analyses.html',{'promos':promos})

def promotion_list(request):
    promotions = Promotion.objects.order_by('order', 'id')
    return render (request,'promotions.html',{'promotions':promotions})

def about (request):
    events = HistoryEvent.objects.all()
    reviews = Review.objects.filter(is_approved = True)[:2]
    return render(request,'about.html',{'events':events,'reviews':reviews})

def service(request):
    items = ServiceItem.objects.filter(category='service')
    return render(request,'services.html',{'items':items})

def diagnostic(request):
    items = ServiceItem.objects.filter(category='diagnostic')
    return render(request,'diagnostics.html',{'items':items})