from django.contrib import admin

# Register your models here.
from place.models import Category, Place, Sehir, Ulke, Images, Comment
class PlaceImageInline(admin.TabularInline):
    model = Images
    extra = 5

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'image_tag']
    readonly_fields = ('image_tag',)
    list_filter = ['status']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Category, CategoryAdmin)

class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'image_tag']
    readonly_fields = ('image_tag',)
    list_filter = ['status', 'category']
    inlines = [PlaceImageInline]
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Place, PlaceAdmin)

class SehirAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
admin.site.register(Sehir, SehirAdmin)

class UlkeAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
admin.site.register(Ulke, UlkeAdmin)

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'place', 'image', 'image_tag']
    readonly_fields = ('image_tag',)
admin.site.register(Images, ImagesAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'comment', 'place', 'user', 'status']
    list_filter = ['status']
admin.site.register(Comment,CommentAdmin)

