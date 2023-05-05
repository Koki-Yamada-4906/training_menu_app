from django.shortcuts import render
from .forms import SignupForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def template_view(request):

    return render(request, 'index.html')


#アカウント登録処理
def signup_view(request):
    if request.method == 'POST':

        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = SignupForm()
    
    param = {
        'form': form
    }

    return render(request, 'signup.html', param)

#ログイン処理
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            
            if user:
                login(request, user)
                
    else:
        form = LoginForm()
         
    param = {
        'form': form,
    }
    
    return render(request, 'login.html', param)
#ログアウト処理
def logout_view(request):
    logout(request)
    
    return render(request, 'logout.html')

#ログインユーザー情報表示処理
@login_required #デコレーター ログインのチェック機能
def user_view(request):
    user = request.user
    
    params = {
        'user': user
    }
    
    return render(request, 'user.html', params)

#他ユーザー表示処理
@login_required
def other_view(request):
    users = User.objects.exclude(username=request.user.username)

    params = {
        'users': users
    }

    return render(request, 'other.html', params)

#アンケート画面
def opinionaire_view(request):
    
    return render(request, 'opinionaire.html')


