from django.shortcuts import render


def user(request):
    return render(request, 'card/user.html')


def home(request):
    return render(request, 'card/home.html')
