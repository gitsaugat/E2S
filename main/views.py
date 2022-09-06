from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'main/home.html')


def settings(request):
    return render(request, 'main/settings.html')


def maps(request):
    return render(request, 'main/map.html')


def email_status(request):
    return render(request, 'main/emailstatus.html')


def sms_status(request):
    return render(request, 'main/smsstatus.html')


def vehicles(request):
    return render(request, 'main/vehicles.html')
