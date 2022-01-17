from django.shortcuts import render

# Create your views here.

def home(request, *args, **kwargs):
    kontextus = {
    }
    return render(request, "home.html", kontextus)
