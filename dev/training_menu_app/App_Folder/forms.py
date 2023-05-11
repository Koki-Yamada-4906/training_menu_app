from django import forms
from django.db import models
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
    FREQUENCY_CHOICES = (
        ('', '----'),
        ('1回', '1回'),
        ('2回', '2回'),
        ('3回', '3回'),
        ('4回', '4回'),
        ('5回', '5回'),
        ('6回以上', '6回以上'),
    )
    PERIOD_CHOICES = (
        ('', '----'),
        ('30', '30分以内'),
        ('60', '60分以内'),
        ('90', '90分以内'),
        ('120', '120分以内'),
        ('180', '180分以内'),
        ('240', '240分以内'),
        ('300', '300分以内'),
        ('それ以上', 'それ以上'),
    )
    DIVIDION_CHOICES = (
        ('全身法', '全身法'),
        ('分割法', '分割法'),
    )
    LIKE_CHOICES = (
        ('', '----'),
        ('胸', '胸'),
        ('背中', '背中'),
        ('脚', '脚'),
        ('肩', '肩'),
        ('腕', '腕'),
        ('腹筋', '腹筋'),
        ('特になし', '特になし'),
    )
    DISLIKE_CHOICES = (
        ('', '----'),
        ('胸', '胸'),
        ('背中', '背中'),
        ('脚', '脚'),
        ('肩', '肩'),
        ('腕', '腕'),
        ('腹筋', '腹筋'),
        ('特になし', '特になし'),
    )
    APPARATUS_CHOICES = (
        ('フリーウェイト', 'フリーウェイト'),
        ('マシン', 'マシン'),
    )
    PURPOSE_CHOICES = (
        ('筋肥大', '筋肥大'),
        ('筋力増強', '筋力増強'),
        ('シェイプアップ', 'シェイプアップ'),
    )
    frequency = forms.ChoiceField(choices=FREQUENCY_CHOICES, label='Q1.週に何回ジムに行けますか？', widget=forms.widgets.Select, required=True)
    period = forms.fields.ChoiceField(choices=PERIOD_CHOICES, label='Q2.1回のトレーニングにどれくらい時間をかけられますか？', widget=forms.widgets.Select, required=True)
    division = forms.fields.ChoiceField(choices=DIVIDION_CHOICES, widget=forms.widgets.Select, required=True)
    like = forms.fields.ChoiceField(choices=LIKE_CHOICES, label='Q4.特に鍛えたい部位はありますか？', widget=forms.widgets.Select, required=True)
    dislike = forms.fields.ChoiceField(choices=DISLIKE_CHOICES, label='Q5.特に鍛えたくない部位はありますか？', widget=forms.widgets.Select, required=True)
    apparatus = forms.fields.ChoiceField(choices=APPARATUS_CHOICES, widget=forms.widgets.Select, required=True)
    purpose = forms.fields.ChoiceField(choices=PURPOSE_CHOICES, widget=forms.widgets.Select, required=True)
    
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
    
    def clean_frequency(self):
        frequency = self.cleaned_data['frequency']
        return frequency
    
    def clean_period(self):
        period = self.cleaned_data['period']
        # periodに対する変換処理
        return period

    def clean_division(self):
        division = self.cleaned_data['division']
        # divisionに対する変換処理
        return division

    def clean_like(self):
        like = self.cleaned_data['like']
        # likeに対する変換処理
        return like

    def clean_dislike(self):
        dislike = self.cleaned_data['dislike']
        # dislikeに対する変換処理
        return dislike

    def clean_apparatus(self):
        apparatus = self.cleaned_data['apparatus']
        # apparatusに対する変換処理
        return apparatus

    def clean_purpose(self):
        purpose = self.cleaned_data['purpose']
        # purposeに対する変換処理
        return purpose
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
