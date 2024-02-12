from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        email = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        messages.success(request, "Your account has been successful created.")
        return render(request, 'login.html')
    
    return render(request, 'register.html')

def login(request):
    return render(request, "login.html")
