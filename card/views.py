from django.shortcuts import render
from .models import New

def user(request):
    # p = New(id_user=1, fio='Абакаров Руслан Магомедович', liga="Золотая лига",
    #         raiting=72, photo='IMG_9402.png')
    # p.save()
    # p = New(id_user=2, fio='Анисимова Виктория Александровна', liga="Бронзовая лига",
    #         raiting=39, photo='IMG_9399.png')
    # p.save()
    # p = New(id_user=3, fio='Гречаник Оксана Андреевна', liga="Серебряная лига",
    #         raiting=44, photo='IMG_9400.png')
    # p.save()
    # p = New(id_user=4, fio='Дроздова Ксения Дмитриевна', liga="Бронзовая лига",
    #         raiting=35, photo='IMG_9419.png')
    # p.save()
    # p = New(id_user=5, fio='Кудрявцев Илья Антонович', liga="Сапфировая лига",
    #         raiting=83, photo='IMG_9411.png')
    # p.save()
    # p = New(id_user=6, fio='Кузнецова Алина Константиновна', liga="Золотая лига",
    #         raiting=77, photo='IMG_9397.png')
    # p.save()
    # p = New(id_user=7, fio='Шаповалова Валерия Павловна', liga="Клубная лига",
    #         raiting=16, photo='IMG_9401.png')
    # p.save()
    # p = New(id_user=8, fio='Кудинова Софья Владимировна', liga="Сапфировая лига",
    #         raiting=92, photo='IMG_9393.png')
    # p.save()
    # p = New(id_user=9, fio='Печенкина Дарья Антоновна', liga="Серебряная лига",
    #         raiting=54, photo='IMG_9396.png')
    # p.save()
    # p = New(id_user=10, fio='Шевчук Егор Александрович', liga="Алмазная лига",
    #         raiting=107, photo='IMG_9395.png')
    # p.save()
    # p = New(id_user=11, fio='Ананьева Ксения Павловна', liga="Сапфировая лига",
    #         raiting=76, photo='IMG_9394.png')
    # p.save()
    # p = New(id_user=12, fio='Нискова Диана Андреевна', liga="Клубная лига",
    #         raiting=19, photo='IMG_9392.JPG')
    # p.save()

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
    print(data['photo'])
    return render(request, 'card/user.html', data)


def home(request):
    return render(request, 'card/home.html')

def about_us(request):
    return render(request, 'card/aboutus.html')

def gallery(request):
    return render(request, 'card/gallery.html')

def calendar(request):
    return render(request, 'card/calendar.html')
