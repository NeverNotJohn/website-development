# our own custom url file!

from django.urls import path
from app2 import views

urlpatterns = {
    path('', views.wow, name='wow')
}