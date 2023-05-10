from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'p-1'})
        self.fields['password'].widget.attrs.update({'class': 'p-1'})
        
class OpinionaireForm(forms.Form):
    FREQUENCY_CHOICES = [
    ('', '----'),
    ('1', '1回'),
    ('2', '2回'),
    ('3', '3回'),
    ('4', '4回'),
    ('5', '5回'),
    ('6', '6回以上'),
    ]
    PERIOD_CHOICES = [
        ('', '----'),
        ('30', '30分以内'),
        ('60', '60分以内'),
        ('90', '90分以内'),
        ('120', '120分以内'),
        ('180', '180分以内'),
        ('240', '240分以内'),
        ('300', '300分以内'),
        ('301', 'それ以上'),
    ]
    LIKE_CHOICES = [
        ('', '----'),
        ('胸', '胸'),
        ('背中', '背中'),
        ('脚', '脚'),
        ('肩', '肩'),
        ('腕', '腕'),
        ('腹筋', '腹筋'),
        ('特になし', '特になし'),
    ]
    DISLIKE_CHOICES = [
        ('', '----'),
        ('胸', '胸'),
        ('背中', '背中'),
        ('脚', '脚'),
        ('肩', '肩'),
        ('腕', '腕'),
        ('腹筋', '腹筋'),
        ('特になし', '特になし'),
    ]
    frequency = forms.ChoiceField(choices=FREQUENCY_CHOICES, label='Q1.週に何回ジムに行けますか？', widget=forms.RadioSelect)
    period = forms.ChoiceField(choices=PERIOD_CHOICES, label='Q2.1回のトレーニングにどれくらい時間をかけられますか？', widget=forms.RadioSelect)
    division = forms.ChoiceField(choices=[('1', '全身法'), ('2', '分割法')], widget=forms.RadioSelect)
    like = forms.ChoiceField(choices=LIKE_CHOICES, label='Q4.特に鍛えたい部位はありますか？', widget=forms.RadioSelect)
    dislike = forms.ChoiceField(choices=DISLIKE_CHOICES, label='Q5.特に鍛えたくない部位はありますか？', widget=forms.RadioSelect)
    apparatus = forms.ChoiceField(choices=[('1', 'フリーウェイト'), ('2', 'マシン')], widget=forms.RadioSelect)
    purpose = forms.ChoiceField(choices=[('1', '筋肥大'), ('2', '筋力増強'), ('3', 'シェイプアップ')], widget=forms.RadioSelect)
    