from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),
    path('yer_gir', views.yer_gir, name='yer_gir'),
    path('yer_sil/<int:id>/<slug:slug>/', views.yer_sil, name='yer_sil'),
]