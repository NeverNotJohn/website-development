from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def index(request):
    my_dict = {'insert_me': 'Hello i am from hello_world app!'}
    return render(request, 'Hello_World/index.html', context=my_dict)