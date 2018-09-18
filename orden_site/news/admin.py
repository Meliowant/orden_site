from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import News, Photo


#class PhotoInline(admin.StackedInline):
class PhotoInline(admin.TabularInline):
    model = Photo
#    fields = ('image_tag',)
    readonly_fields = ('image_tag','delete_im')
    extra = 1
    delete = 'true'

"""
class NewsAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'pub_date']
    inlines = [PhotoInline]
"""

class NewsAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    fields = ['title', 'content', 'pub_date']
    inlines = [PhotoInline]


admin.site.register(News, NewsAdmin)
admin.site.register(Photo)


# Register your models here.
