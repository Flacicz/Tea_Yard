from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Имя пользователя', widget=forms.TextInput(
            attrs={'class': 'form-control', 'autofocus': 'off'}
        )
    )
    password = forms.CharField(
        label='Пароль', widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'autofocus': 'off'}
        )
    )


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя', max_length=50, help_text='Максимум 50 символов', widget=forms.TextInput(
            attrs={'class': 'form-control', 'autofocus': 'off'}
        )
    )
    password1 = forms.CharField(
        label='Пароль', widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'autofocus': 'off'}
        )
    )
    password2 = forms.CharField(
        label='Подтверждение пароля', widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'autofocus': 'off'}
        )
    )
    email = forms.EmailField(
        label='E-mail', widget=forms.EmailInput(
            attrs={'class': 'form-control', 'autofocus': 'off'}
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
