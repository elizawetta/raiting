from django.shortcuts import render
from .models import New

def user(request):
    id_user = request.GET.get("id", -1)
    if len(New.objects.filter(id_user=id_user)) == 0:
        return render(request, 'card/notfound.html')
    man = New.objects.filter(id_user=id_user)[0]
    data = {
        'fio': man.fio,
        'raiting': man.raiting,
        'comp': man.comp
    }
    return render(request, 'card/user.html', data)


def home(request):
    return render(request, 'card/home.html')

def about_us(request):
    return render(request, 'card/aboutus.html')

def gallery(request):
    return render(request, 'card/gallery.html')

def calendar(request):
    return render(request, 'card/calendar.html')
