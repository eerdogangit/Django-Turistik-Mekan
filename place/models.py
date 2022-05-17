from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )

    title = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='catimages/')
    status = models.CharField(max_length=10, choices=STATUS)

    slug = models.SlugField()
    parent = models.ForeignKey('self',blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Sehir(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )

    title = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS)

    def __str__(self):
        return self.title

class Ulke(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )

    title = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS)

    def __str__(self):
        return self.title

class Place(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # sonradan ekledim
    title = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='placeimages/')
    detail = models.TextField()
    slug = models.SlugField(blank=True)

    sehir = models.ForeignKey(Sehir, on_delete=models.CASCADE, blank=True, null=True)
    ulke = models.ForeignKey(Ulke, on_delete=models.CASCADE, blank=True, null=True)

    adres = models.CharField(max_length=255, blank=True)
    telefon = models.CharField(max_length=255, blank=True)
    email = models.CharField(blank=True, max_length=255)
    facebook = models.CharField(blank=True, max_length=255)
    twitter = models.CharField(blank=True, max_length=255)
    instagram = models.CharField(blank=True, max_length=255)

    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Images(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(blank=True, upload_to='galimages/')

    def __str__(self):
        return self.title

    #def image_tag(self):
    #    return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    #image_tag.short_description = 'Image'