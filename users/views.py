from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegister, UserUpdateForm, ProfileUpdateForm


def register(request):
    """
    User registration view
    Redirects to the login page once a user is registered
    """
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account has been created for {username}!. You can now log in.")
            return redirect("login")
    else:
        form = UserRegister()
    return render(request=request, template_name="users/register.html", context={"form": form})

@login_required
def profile(request):
    """
    Visalize a user profile - requires a login
    """
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your profile has been updated!")
            return redirect("profile")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        "u_form": u_form,
        "p_form": p_form
    }

    return render(request, "users/profile.html", context=context)