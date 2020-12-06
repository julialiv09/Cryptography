from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .functions import *


def index(request):
    if request.method == "POST":
        login = request.POST.get("login")
        password = request.POST.get("password")
        email = find_user(login, password)
        if email == "Wrong password" or email == "User not found":
            return render(request, "bad.html")
        send_code(email)
        # userform = UserForm2()
        return HttpResponseRedirect("input_code")
        # return render(request, "auth.html", {"form": userform})

        # name = request.POST.get("name")
        # age = request.POST.get("age")     # получение значения поля age
        # return HttpResponse("<h2>Hello, {0}</h2>".format(name))
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})


def auth(request):
    if request.method == "POST":
        code = request.POST.get("code")
        if authentication(code) == "auth_ok":
            return render(request, "ok.html")
        else:
            userform = UserForm2()
            return render(request, "auth.html", {"form": userform})
    else:
        userform = UserForm2()
        return render(request, "auth.html", {"form": userform})