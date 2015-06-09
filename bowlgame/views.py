from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import BowlGameForm, PlayerForm
from .models import BowlGame
# Create your views here.

def home(request):
    title = 'BowlGame'
    form = BowlGameForm(request.POST or None)
    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context = {
            "title": "Thank You!"
        }
    return render(request, "home.html", context)

def bowlgames(request):
    queryset = BowlGame.objects.all().order_by('-bowl')
    context = {
        "queryset": queryset
    }
    return render(request, "bowlgames.html", context)

def userhome(request):
    usertitle = 'BowlGame'
    context = {
        "title": usertitle}
    return render(request, "userhome.html", context)




def username(request):
    username = Player.username
    context = {
        "username": username
    }
    return render(username())