from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from place.models import  CommentForm, Comment
def index(request):
    return HttpResponse("Place Page")

@login_required(login_url='/login') #login check
def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user=request.user

            data = Comment()
            data.user_id = current_user.id
            data.place_id = id
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Yorumunuz başarıyla gönderilmiştir. Teşekkür ederiz")

            return HttpResponseRedirect(url)
    messages.warning(request, "Yorumunuz kaydedilemedi.")
    return HttpResponse("Kaydetme İşlemi Gerçekleşmedi")
