import logging
from django.shortcuts import render
from .forms import SignupForm, LoginForm, OpinionaireForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

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
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('App:list'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'login.html')
    
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
    if request.method == 'POST':
        frequency = request.POST.get('FREQUENCY_CHOICES')
        period = request.POST.get('PERIOD_CHOICES')
        division = request.POST.get('DIVIDION_CHOICES')
        like = request.POST.get('LIKE_CHOICES')
        dislike = request.POST.get('DISLIKE_CHOICES')
        apparatus = request.POST.get('APPARATUS_CHOICES')
        purpose = request.POST.get('PURPOSE_CHOICES')

        return render(request, 'result.html', {'frequency': frequency, 'period': period, 'division': division, 'like': like, 'dislike': dislike, 'apparatus': apparatus, 'purpose': purpose})

    else:
        form = OpinionaireForm()

    return render(request, 'opinionaire.html', {'form': form})       
    
    
    # if request.method == 'GET':
    #     return render(request, 'opinionaire.html', {'form': OpinionaireForm()})
   
    # elif request.method == 'POST':
    #     form = OpinionaireForm(request.POST)
    #     if not form.is_valid():
    #         return render(request, 'opinionaire.html', {'form': form, 'errors': form.errors})
        
    #     frequency = form.cleaned_data['frequency']
    #     period = form.cleaned_data['period']
    #     division = form.cleaned_data['division']
    #     like = form.cleaned_data['like']
    #     dislike = form.cleaned_data['dislike']
    #     apparatus = form.cleaned_data['apparatus']
    #     purpose = form.cleaned_data['purpose']
    #     return render(request, 'result.html', {'frequency': frequency, 'period': period, 'division': division, 'like': like, 'dislike': dislike, 'apparatus': apparatus, 'purpose': purpose})
  
      


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # if request.method == 'POST':
    #     form = OpinionaireForm(request.POST)
    #     if form.is_valid():
    #         frequency = form.cleaned_data['frequency']
    #         period = form.cleaned_data['period']
    #         division = form.cleaned_data['division']
    #         like = form.cleaned_data['like']
    #         dislike = form.cleaned_data['dislike']
    #         apparatus = form.cleaned_data['apparatus']
    #         purpose = form.cleaned_data['purpose']

    #         print(frequency)
    #         print(period)
    #         print(division)
    #         print(like)
    #         print(dislike)
    #         print(apparatus)
    #         print(purpose)

    #         return render(request, 'result.html')
    # else:
    #     form = OpinionaireForm()

    # return render(request, 'opinionaire.html', {'form': form})
