from django.urls import path

from formapp import views

urlpatterns = [
    path('1/', views.contact1, name='contact1'),
]