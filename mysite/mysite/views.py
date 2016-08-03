from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail
import string
import random
# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    try:
        Username = request.POST['email']
        Password = request.POST['password']
        Password2 = request.POST['password2']
        if Password != Password2:
            return render(request, 'new login.html', {
                'error':'Passwords are not the same.'
                })
        else:
            if User.objects.filter(username = Username).exists():
                user = authenticate(username = Username, password = Password)
                if user is None:
                    return render(request, 'new login.html', {
                        'error':'Username has already existed. Please choose another name.'
                    })
                else:
                    login(request, user)
                    return HttpResponseRedirect('/')
            else:
                """send_mail(
                    'Confirm your email',
                    'Hello',
                    settings.EMAIL_HOST_USER,
                    [User],
                    fail_silently = False
                )"""
                user = User.objects.create_user(Username, Username, Password)
                user.save()
                user = authenticate(username = Username, password = Password)
                login(request, user)
                return HttpResponseRedirect('/')
    except:
        return render(request, 'new login.html')
    else:
        return render(request, 'new login.html')

def Login(request):
    try:
        Username = request.POST['email']
        Password = request.POST['password']
        user = authenticate(username = Username, password = Password)
        if user is not None:
            login(request, user)
            Next = request.POST["next"]
            if Next != "":
                return HttpResponseRedirect(Next)
            else:
                return HttpResponseRedirect('/')
        else:
            context = {
            'error':"Invalid email or password"
            }
            return redirect('/login', context)
    except:
        return render_to_response('login.html', {'from':request.GET.get('from', None)})
    else:
        return render(request, 'new login.html')

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def forget_password(request):
    try:
        Username = request.POST['email']
        user = User.objects.get(username = Username)
        if user is None:
            context = {
            'error':"Account does not exist!"
            }
            return render(request, 'login.html', context)
        else:
            new_password = ''.join(random.SystemRandom().choice(string.digits) for _ in range(10))
            user.set_password(new_password)
            user.save()
            user = authenticate(username = Username, password = new_password)
            login(request, user)
            context = {
            'error':"New Password : " + new_password
            }
            return render(request, 'login.html', context)
    except:
        return render(request, 'forget_password.html')
    else:
        return render(request, 'forget_password.html')

def explain(request):
    return render(request, 'explain.html')