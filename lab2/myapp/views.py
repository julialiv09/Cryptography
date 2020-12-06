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
        return HttpResponseRedirect("input_code")
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
