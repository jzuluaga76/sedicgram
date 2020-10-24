from django.contrib import admin
from Users.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
     list_display = ('user','website','biography','Phone_number','create','modify')
     list_display_link = ('user','title')
     list_aditable = ('biography','phone_number')