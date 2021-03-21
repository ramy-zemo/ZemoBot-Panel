from django.shortcuts import render


def register_view(request, *args, **kwargs):
    return render(request, "register.html", {})


def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})
