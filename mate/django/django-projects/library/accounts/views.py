from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def login_view(request):
    print(request.user)
    if request.method == "GET":
        return render(request, "accounts/login.html")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)  # в текущуюу сессию присваиваю того юзера к-го проатутентифицировал, это и есть логин
            return HttpResponseRedirect(reverse("catalog:index"))
        else:
            error_context = {
                "errors": "Invalid credentials"
            }
        return render(request, "accounts/login.html", context=error_context)


def logout_view(request):
    # Remove the authenticated user's ID from the request and flush their session data.
    logout(request)
    return render(request, "accounts/logged_out.html")
