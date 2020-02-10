from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from authorization.forms import SignUpForm


def signup(request):
    if request.user.is_authenticated == False:
        context = {}
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                auth_login(request, user)
                return redirect('/')
        else:
            form = SignUpForm()
        context['form'] = form
        return render(request, 'signup.html', context)
    else:
        return redirect('/')


def login(request):
    if request.user.is_authenticated == False:
        context = {}
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                fw_username = form.cleaned_data['username']
                fw_password = form.cleaned_data['password']
                user = authenticate(username=fw_username, password=fw_password)
                if user is not None:
                    if user.is_active:
                        auth_login(request, user)
                return redirect('/')
        else:
            form = AuthenticationForm()
        context['form'] = form
        return render(request, 'login.html', context)
    else:
        return redirect('/')


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('/')

def page(request):
    return render (request, 'page.html')
