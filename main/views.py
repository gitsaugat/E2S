from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'main/home.html')


def settings(request):
    return render(request, 'main/settings.html')


def maps(request):
    return render(request, 'main/map.html')
