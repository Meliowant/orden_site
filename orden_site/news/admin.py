from django.contrib import admin

from .models import News, Photo

#class PhotoInline(admin.StackedInline):
class PhotoInline(admin.TabularInline):
    model = Photo
#    fields = ('image_tag',)
    readonly_fields = ('image_tag','delete_im')
    extra = 1
    delete = 'true'

class NewsAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'pub_date']
    inlines = [PhotoInline]

admin.site.register(News, NewsAdmin)
admin.site.register(Photo)


# Register your models here.
