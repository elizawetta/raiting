from django.shortcuts import render


def user(request):
    id_user = request.GET.get("id", 0)
    return render(request, 'card/user.html', {'id': id_user})


def home(request):
    return render(request, 'card/home.html')
