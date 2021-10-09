from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # 장고에서 제공하는 사용자 모델, 장고 인증과 연결


def signup(request):
    if request.method == 'POST':
        username = request.POST['username'],
        email = request.POST['email'],
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            User.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
            return redirect('accounts:login')
        else:
            context = {'error': '비밀번호 일치하지 않다.'}
            return render(request, 'accounts/signup.html', context)
    else:
        return render(request, 'accounts/signup.html')
