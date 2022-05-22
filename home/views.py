from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
#from home.forms import SearchForm, SignUpForm
#from home.models import Setting, ContactFormMessage, Profile, Faq
from home.models import Setting, ContactFormu, ContactFormMessage
from place.models import Place, Category, Images

def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Place.objects.all()[:3]
    category = Category.objects.all()
    places = Place.objects.all().order_by('-id')[:12]

    context = {'setting': setting,
               'category': category,
               'page': 'home',
               'sliderdata': sliderdata,
               'places': places
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
    if request.method == 'POST': #form post olduysa
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage() #model ile bağlantı kur
            data.firstname = form.cleaned_data['firstname'] #formdan bilgiyi al
            data.lastname = form.cleaned_data['lastname']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save() #kaydet
            messages.success(request, "Mesajınız başarıyla gönderilmiştir. Teşekkür ederiz")
            return HttpResponseRedirect ('/iletisim')

    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    category = Category.objects.all()
    context = {'setting': setting,
               'form':form,
               'category': category,
               'page':'iletisim'}
    return render(request, 'iletisim.html', context)
