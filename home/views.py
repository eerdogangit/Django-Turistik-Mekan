from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
#from home.forms import SearchForm, SignUpForm
#from home.models import Setting, ContactFormMessage, Profile, Faq
from home.models import Setting
from place.models import Place, Category, Images

def index(request):
    setting = Setting.objects.get(pk=1)
    #sliderdata = Place.objects.all()[:3]
    category = Category.objects.all()
    places = Place.objects.all().order_by('-id')[:12]

    context = {'setting': setting,
               'category': category,
               'page': 'home',
               #'sliderdata': sliderdata,
               'rents': places
               }
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting,
               'category': category,
               'page':'hakkimizda'}
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting,
               'category': category,
               'page':'referanslar'}
    return render(request, 'referanslar.html', context)
def iletisim(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting,
               'category': category,
               'page':'iletisim'}
    return render(request, 'iletisim.html', context)
