from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from clinic.models import Patient
from .forms import LoginForm, RegisterForm


def login_view(request):
    if request.user.is_authenticated:
        if request.user.is_staff or request.user.is_superuser:
            return redirect("dashboard")
        return redirect("home")

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        identifier = request.POST.get("username")
        password = request.POST.get("password")

        # 1. Try finding user by Email
        user_obj = User.objects.filter(email__iexact=identifier).first()

        # 2. If not found by email, search by Phone in Patient records
        if not user_obj:
            patient = Patient.objects.filter(phone=identifier).first()
            if patient and patient.email:
                user_obj = User.objects.filter(email__iexact=patient.email).first()

        # 3. Authenticate user if found
        if user_obj:
            user = authenticate(request, username=user_obj.username, password=password)
            if user:
                login(request, user)
                messages.success(request, f"Welcome back, {user.first_name or user.username}!")
                if user.is_staff or user.is_superuser:
                    return redirect("dashboard")
                return redirect("home")

        # Fallback standard authentication
        user = authenticate(request, username=identifier, password=password)
        if user:
            login(request, user)
            if user.is_staff or user.is_superuser:
                return redirect("dashboard")
            return redirect("home")

        messages.error(request, "Invalid Email/Phone number or password.")
    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account registered successfully!")
            return redirect("home")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect("home")