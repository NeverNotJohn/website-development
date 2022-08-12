from django.urls import path
from one import views

urlpatterns = {
    path('god/', views.no, name="no"),
    path('', views.help, name="help")
}