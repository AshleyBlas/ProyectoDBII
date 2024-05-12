from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Perfil


# Create your views here.
def index(request):
    return render(request, "ANEA/index.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "ANEA/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "ANEA/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


