from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:new_id>/', views.detail, name='detail'),
]