from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def add(response):
    if response.method == 'POST':
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(response, 'add.html', {'form': form})


def home(response):
    return render(response, 'members.html', {})

@login_required
def chat(response):
    return render(response, 'chat.html', {'username': response.user.username})
