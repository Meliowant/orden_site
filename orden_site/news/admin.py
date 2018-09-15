from django.contrib import admin

from .models import News, Photo

class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1

class NewsAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'pub_date']
    inlines = [PhotoInline]

admin.site.register(News, NewsAdmin)
admin.site.register(Photo)


# Register your models here.
