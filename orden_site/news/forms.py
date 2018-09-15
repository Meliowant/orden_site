from django import forms

from .models import News, Photo

class AddNew(forms.Form):
	title = forms.CharField(max_length=200)
	content = forms.CharField(widget=forms.Textarea)
	photos = forms.ImageField(label=u'Фотографії', widget=forms.FileInput(attrs={'multiple': 'multiple'}))

#    class Meta:
#        model = News
#        fields = ('title', 'content',)