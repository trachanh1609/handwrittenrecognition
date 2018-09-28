from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('make_prediction/', views.make_prediction, name='make_prediction'),
]