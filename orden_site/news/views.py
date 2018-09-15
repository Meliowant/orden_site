from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import News

# Create your views here.
def index(request):
    latest_news_list = News.objects.order_by('-pub_date')#[:5]
    template = loader.get_template('news/index.html')
    context = {
        'latest_news_list': latest_news_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, new_id):
    news_list = News.objects.get(pk=new_id) #.order_by('-id')#[:5]
    return HttpResponse("You're looking at new: %s." % news_list.content)

def add(request):
    if request.method == 'GET':
        form = AddNew()
        return render(request, 'news/add.html', {'form': form})
    elif request.method == 'POST':
        form = AddNew(request.POST, request.FILES)
        if form.is_valid():
            new = News.objects.create(title=form.cleaned_data['title'], content=form.cleaned_data['content'], pub_date = timezone.now())
            new.save()
            for f in request.FILES.getlist('photos'):
                data = f.read() #Если файл целиком умещается в памяти
                photo = Photo(new=new)
                photo.image.save(f.name, ContentFile(data))
                photo.save()
            return redirect('')
        else:
            return render(request, 'news/add.html', {'form': form})