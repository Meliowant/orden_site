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
