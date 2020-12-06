from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('input_code', views.auth, name='auth')
]