from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from .forms import AddNew
from .models import News, Photo
from django.utils import timezone
from django.core.files.base import ContentFile

# Create your views here.
def index(request):
    latest_news_list = News.objects.order_by('-pub_date')
    template = loader.get_template('news/index.html')
    context = {
        'latest_news_list': latest_news_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, new_id):
    new = News.objects.get(pk=new_id)
    p_list = Photo.objects.filter(new=new)
    template = loader.get_template('news/detail.html')
    context = {'new': new,'p_list': p_list}
    return HttpResponse(template.render(context, request))

def add(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            form = AddNew()
            return render(request, 'news/add.html', {'form': form})
        elif request.method == 'POST':
            form = AddNew(request.POST, request.FILES)
            if form.is_valid():
                new = News.objects.create(title=form.cleaned_data['title'], content=form.cleaned_data['content'], pub_date = timezone.now())
                new.save()
                for f in request.FILES.getlist('photos'):
                    data = f.read()
                    photo = Photo(new=new)
                    photo.image.save(f.name, ContentFile(data))
                    photo.save()
                return redirect('/news/%d/'%new.id)
        else:
            return render(request, 'news/add.html', {'form': form})
    else: 
        return HttpResponse("Oops")
