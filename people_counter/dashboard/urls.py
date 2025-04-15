from django.urls import path

from . import views

urlpatterns = [
    path('details/<int:pk>', views.details, name='details'),
    path('', views.dashboard, name='dashboard'),
]