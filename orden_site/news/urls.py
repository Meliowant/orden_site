from django.urls import path

from orden_site.lytsar import views

urlpatterns = [
    path('', views.index, name='index')
]