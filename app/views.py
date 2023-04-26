from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

# User Registration
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.success(request, "Password and Confirm Password didn't match!!")
        else:
            user = User.objects.create_user(username, email, password1)
            user.save()
            return redirect('login')
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')
