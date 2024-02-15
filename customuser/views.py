from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import User
from book.views import home



# Create your views here.

def index(request):
    if request.method == "GET":
        return render(request, "authntication/login.html")

    email = request.POST.get('email')
    password = request.POST.get('password')
    
    user = authenticate(username = email , password = password)
    
    if user:
        request.session['username']= user.get_username()
        return redirect(home)
    else:
        messages.warning(request, "login failed")
    
    return redirect(index)
    
    

def signup(request):
    if request.method == "GET":
        return  render(request, "authntication/signup.html")
    
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')
    
    try:
        User.objects.get(email=email)
        messages.warning(request, "An account already exists with this email")
        return redirect('signup')
    except Exception:
        pass 


    if password != confirm_password:
        messages.warning(request, "Password must match")
        return redirect(signup)
    
    user = User.objects.create_user(email = email , password = password)
    if user:
        messages.success(request, "registered successfully")
        return redirect(index)

    
    messages.warning(request, "registration failed")
    return redirect(signup)

def logout(request):
    request.session['username'] = None
    return redirect(index)

    

    
    
    
    
    