from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    context = {
        "title": "Hola mundo",
        "content": "Bienvenido a la página de inicio"
    }
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "Acerca de..",
        "content": "Bienvenido a la página Acerca de"
    }
    return render(request, "home_page.html", context)

def contact_page(request):
    context = {
        "title": "Contacto",
        "content": "Bienvenido a la página de contacto"
    }
    return render(request, "home_page.html", context)