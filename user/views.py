from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from home.models import Setting, Profile
# Create your views here.
from place.models import Place, Category, Sehir, Ulke
from user.forms import UserUpdateForm, ProfileUpdateForm, Yer_GirForm
from django.contrib import messages


def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    current_user = request.user
    profile = Profile.objects.get(user_id=current_user.id)
    yerler = Place.objects.filter(user_id=current_user.id, status='True')
    context = {'setting': setting,
               'profile': profile,
               'yerler': yerler,
               'category': category,
               }
    return render(request, 'user_profile.html', context)

def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Hesabınız başarıyla güncellendi')
            return redirect('/user')

    else:
            setting = Setting.objects.get(pk=1)

            user_form = UserUpdateForm(instance=request.user)
            profile_form = ProfileUpdateForm(instance=request.user.profile)
            context = {'setting': setting,
                       'user_form': user_form,
                       'profile_form': profile_form
                       }
            return render(request, 'user_update.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Şifreniz güncellendi!')
            return redirect('/user')
        else:
            messages.error(request, 'Please correct the errors below. <br/>' + str(form.errors))
            return redirect('/user/password')
    else:
        setting = Setting.objects.get(pk=1)
        form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {'form': form, 'setting': setting})

def yer_gir(request):
    if request.method == 'POST':
        try:
            title = request.POST['title']
            keywords = request.POST['keywords']
            description = request.POST['description']
            image = request.FILES['image']
            detail = request.POST['detail']
            category = request.POST['category']
            slug = request.POST['slug']
            current_user = request.user
            sehir = request.POST['sehir']
            ulke = request.POST['ulke']
            adres = request.POST['adres']
            telefon = request.POST['telefon']
            email = request.POST['email']
            facebook = request.POST['facebook']
            twitter = request.POST['twitter']
            instagram = request.POST['instagram']

            Place(title=title, keywords=keywords, description=description, image=image,
                 detail=detail, category_id=category, slug=slug,
                 status=False, user_id=current_user.id, sehir_id=sehir, ulke_id=ulke,
                 adres=adres, telefon=telefon, email=email, facebook=facebook,
                 twitter=twitter, instagram=instagram
                 ).save()

            messages.success(request, 'turistik yer kaydı girildi')
            return redirect('/user/')
        except Exception as e:
            messages.success(request, 'hata var' + str(e))
            return redirect('/user/yer_gir')

    #form = Mulk_GirForm(instance=request.user)
    category = Category.objects.all()
    ulke = Ulke.objects.all()
    sehir = Sehir.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'category': category,
               'ulke': ulke,
               'sehir': sehir
               }
    return render(request, 'yer_gir.html', context)

def yer_sil(request, id, slug):
    yer = Place.objects.get(id=id)
    yer.delete()
    messages.success(request, 'Kayıt silindi')
    return redirect('/user/')