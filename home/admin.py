from django.contrib import admin

from home.models import Setting, ContactFormMessage, Profile, Faq

class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email', 'message', 'status']
    list_filter = ['status']
admin.site.register(ContactFormMessage, ContactFormMessageAdmin)
admin.site.register(Setting)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'image_tag', 'phone', 'address']
admin.site.register(Profile, ProfileAdmin)

class FaqAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'status']
    list_filter = ['status']
admin.site.register(Faq,FaqAdmin)