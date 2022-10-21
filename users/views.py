from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request,
                f"Account created for user {username}! You are now able to login",
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", context={"form": form})


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    return render(request, "users/profile.html")
