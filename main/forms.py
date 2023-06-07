from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Question, News
from django import forms


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('first_name', 'email', 'message')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Есіміңіз'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Почтаңыз'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Хабарлама мәтіні'}),
        }


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Есіміңіз"}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Тегіңіз"}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Логин"}))

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Құпия сөз"}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Құпия сөзді қайталаңыз"}))

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "+7 708 000 00 00"}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'phone')


class LoginForm(forms.ModelForm):
    login = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Логин"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Құпия сөз"}))

    class Meta:
        model = User
        fields = ('login', 'password',)


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'image', 'description', )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тақырыбы'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Сипаттама'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Сурет'}),
        }


