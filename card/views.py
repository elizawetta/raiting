from django.shortcuts import render
from .models import New

def user(request):
    id_user = request.GET.get("id", -1)
    if len(New.objects.filter(id_user=id_user)) == 0:
        return render(request, 'card/notfound.html')
    user_ = New.objects.filter(id_user=id_user)[0]
    colors = {
        'Бронзовая лига': '#FF8512',
        'Серебряная лига': '#AFAFAF',
        'Сапфировая лига': '#FF00DC',
        'Золотая лига' : '#FFC300',
        'Клубная лига': '#FF0000',
        'Алмазная лига': '#00FFF3'
    }
    data = {
        'fio': user_.fio,
        'liga': user_.liga,
        'raiting': user_.raiting,
        'photo': user_.photo,
        'color': colors[user_.liga]
    }
    return render(request, 'card/user.html', data)

def sort(n1, n2):
    return n1.raiting < n2.raiting
def home(request):
    data = {'data': sorted(New.objects.all(), key=lambda x: -x.raiting)}
    return render(request, 'card/home.html', data)

def about_us(request):
    return render(request, 'card/aboutus.html')

def gallery(request):
    return render(request, 'card/gallery.html')

def calendar(request):
    return render(request, 'card/calendar.html')
