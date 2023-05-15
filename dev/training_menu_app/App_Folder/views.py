import openai
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
        
        response = call_openai_gpt(frequency, period, division, like, dislike, apparatus, purpose)
        
        return render(request, 'result.html', {'response':response})        
    else:
        form = OpinionaireForm()

    return render(request, 'opinionaire.html', {'form': form})       
    
#文章生成
def call_openai_gpt(frequency, period, division, like, dislike, apparatus, purpose):
    openai.api_key = "your api key"
    prompt = "トレーニングのメニューを考えてください。トレーニング内容は横並びで出力してください。出力のフォーマットは、〇回目　・トレーニング名(適切なメニュー数を表示)　としてください。一回のトレーニング時間は{period}です。トレーニング方法は{division}で、{like}の種目を多めに取り入れて、{dislike}の種目は1種目だけ軽めのを取り入れます。{apparatus}をメインにし、目的は{purpose}です。これを踏まえて{frequency}に分けてください。また、そのメニューが何回目かを示してください".format(frequency=frequency, period=period, division=division, like=like, dislike=dislike, apparatus=apparatus, purpose=purpose)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1048,
        n=1,
        stop=None, 
        temperature=0,
    )
    response = (response["choices"][0]["text"]).strip()
     
    # response = "1回目 ・デッドリフト ・レッグプレス ・レッグカール ・バックエクステンション ・ラットプルダウン2回目 ・ショルダープレス ・レッグエクステンション ・レッグカール ・ラットプルダウン ・ラットロウ3回目 ・デッドリフト ・レッグプレス ・レッグエクステンション ・バックエクステンション ・ラットプルダウン4回目 ・ショルダープレス ・レッグプレス ・レッグカール ・バックエクステンション ・ラットロウ5回目 ・デッドリフト ・レッグプレス ・レッグエクステンション ・バックエクステンション ・ラットプルダウン6回目 ・ショルダープレス ・レッグプレス ・レッグカール ・バックエクステンション ・ラットロウ"
    # print(response)
    
    #メニュー文の編集
    targets = ['1回目', '2回目', '3回目', '4回目', '5回目', '6回目', '１回目', '２回目', '３回目', '４回目', '５回目', '６回目']
    for target in targets:
        response = response.replace(target, '</div> <div class="block w-auto p-6 bg-gray-200 border border-gray-200 rounded-lg shadow dark:bg-gray-800 mt-10 mb-5">' + target + '\n')
    
    print(response)
    
    return response

def result_view(request):
    return render(request, 'result.html')


