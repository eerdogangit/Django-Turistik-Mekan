from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm, TextInput, Textarea
from django.utils.safestring import mark_safe

# Create your models here.
class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    address = models.CharField(blank=True, max_length=255)
    phone = models.CharField(blank=True, max_length=255)
    fax = models.CharField(blank=True, max_length=255)
    email = models.CharField(blank=True, max_length=255)
    smtpserver = models.CharField(blank=True, max_length=255)
    smtpemail = models.CharField(blank=True, max_length=255)
    smtppassword = models.CharField(blank=True, max_length=255)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=255)
    twitter = models.CharField(blank=True, max_length=255)
    vine = models.CharField(blank=True, max_length=255)
    instagram = models.CharField(blank=True, max_length=255)
    aboutus = RichTextUploadingField()
    references = RichTextUploadingField()
    contact = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
class ContactFormMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    firstname = models.CharField(blank=True, max_length=255)
    lastname = models.CharField(blank=True, max_length=255)
    email = models.CharField(blank=True, max_length=255)
    phone = models.CharField(blank=True, max_length=255)
    message = models.CharField(blank=True, max_length=255)
    status = models.CharField(max_length=10, choices=STATUS)
    ip = models.CharField(blank=True, max_length=255)
    note = models.CharField(blank=True, max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname
class ContactFormu(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['firstname', 'lastname', 'email', 'phone', 'message']
        widgets = {
            'firstname': TextInput(attrs={'placeholder':'Ad'}),
            'lastname': TextInput(attrs={'placeholder': 'Soyad'}),
            'email': TextInput(attrs={'placeholder': 'E-Posta Adresi'}),
            'phone': TextInput(attrs={'placeholder': 'Telefon Numarası'}),
            'message': Textarea(attrs={'placeholder': 'Mesaj'}),
        }

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=255)
    address = models.CharField(blank=True, max_length=255)
    image = models.ImageField(blank=True, upload_to='userimages/')

    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + ' [' + self.user.username + ']'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class UserProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address', 'image']

class Faq(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    question = models.CharField(max_length=255)
    answer = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question