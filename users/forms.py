from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# user registration form
class UserRegister(UserCreationForm):
    """
    User registration form - 
    ask for a username, email, and password and
    confirm password while registering a user 
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):
    """
    Update a user
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]

class ProfileUpdateForm(forms.ModelForm):
    """
    Update a user profile
    """
    class Meta:
        model = Profile
        fields = ["image"]