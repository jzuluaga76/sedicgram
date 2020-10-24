from django.contrib import admin
from Post.models import Post

# Register your models here.

@admin.register(Post)
class Admin_Post(admin.ModelAdmin):
    list_display = ('user','title','photo', 'postdate', 'modify')
    list_display_link = ('user', 'title')
    list_aditable = ('photo','website')