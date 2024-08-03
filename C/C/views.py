from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request, 'home.html' )
    # return HttpResponse('Hoooray!!!, i am glad to be a pro in this sector!')


def about(request):
    return render(request, 'about.html')
    # return HttpResponse('My About page')