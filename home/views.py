import json

from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from home.forms import SearchForm, SignUpForm
from home.models import Setting, ContactFormu, ContactFormMessage, Profile, Faq
from place.models import Place, Category, Images, Comment

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

def category(request, id, slug):
    rents = Place.objects.get(category=id)
    context = {'places': rents}
    return render(request, 'places.html', context)

def category_places(request, id, slug):
    category = Category.objects.all()
    categoryData = Category.objects.get(pk=id)
    places = Place.objects.filter(category_id=id)
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'page': 'places',
               'places': places,
               'category': category,
               'categoryData': categoryData
               }
    return render(request, 'places.html', context)

def place_detail(request, id, slug):
    setting = Setting.objects.get(pk=1)
    place = Place.objects.get(pk=id)
    images = Images.objects.filter(place_id=id)
    comments = Comment.objects.filter(place_id=id, status='True')
    context = {'setting': setting,
               'place': place,
               'images': images,
               'comments': comments,
               }
    return render(request, 'place_detail.html', context)

def place_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            setting = Setting.objects.get(pk=1)
            category = Category.objects.all()
            query = form.cleaned_data['query']
            places = Place.objects.filter(title__icontains=query)
            context = {'setting': setting,
                    'places': places,
                   'category': category
            }
            return render(request, 'place_search.html', context)

def place_search_auto(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    places = Place.objects.filter(title__icontains=q)
    results = []
    for rs in places:
      place_json = {}
      place_json = rs.title
      results.append(place_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Login Hatası ! Kullanıcı adı ya da şifre yanlış")
            return HttpResponseRedirect('/login')

    setting = Setting.objects.get(pk=1)
    context = {'setting': setting }
    return render(request, 'login.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            
            return HttpResponseRedirect('/')

    form = SignUpForm()
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'form': form
               }
    return render(request, 'signup.html', context)

def faq(request):
    faq = Faq.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'faq': faq
               }
    return render(request, 'faq.html', context)