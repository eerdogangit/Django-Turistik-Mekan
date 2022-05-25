from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import Setting, Profile
# Create your views here.
from place.models import Place, Category


def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    current_user = request.user
    profile = Profile.objects.get(user_id=current_user.id)
    yerler = Place.objects.filter(user_id=current_user.id)
    context = {'setting': setting,
               'profile': profile,
               'yerler': yerler,
               'category': category,
               }
    return render(request, 'user_profile.html', context)

