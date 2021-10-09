from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required


@login_required
def logout(request):
    auth_logout(request)
    return redirect('account:login')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('list')
        else:
            context = {'error': '아이디 또는 비밀번호가 다릅니다.'}
            return redirect(request, 'account/login.html', context)
    else:
        return render(request, 'account/login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
        return redirect('list')
    else:
        context = {'error': '비밀번호가 불일치하다.'}
        return render(request, 'account/signup.html', context)
