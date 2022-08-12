# our own custom url file!

from django.urls import path
from Hello_World import views

urlpatterns = {
    path('', views.index, name='index')
}