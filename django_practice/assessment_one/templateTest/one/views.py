from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def help(response):
    my_dict = {'god': 'Help Me!'}
    return render(response,'one/wow.html', context=my_dict)

def no(response):
    my_dict = {'god': 'PLEASE'}
    return render(response,'one/wow.html', context=my_dict)