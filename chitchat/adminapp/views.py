from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def loginpagecall(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chitchat')  # Redirect to the chitchat page
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'adminapp/loginpage.html')

def registerpagecall(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Account created successfully')
                return redirect('loginpagecall')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'adminapp/registerpage.html')


def logout_view(request):
    logout(request)
    return redirect('loginpagecall')

from .models import Message

def chitchat(request):
    if request.method == 'POST':
        text = request.POST['text']
        message = Message(user=request.user, text=text)
        message.save()
        return redirect('chitchat')

    messages = Message.objects.all().order_by('created_at')
    return render(request, 'adminapp/chitchat.html', {'messages': messages})
