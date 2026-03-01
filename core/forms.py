from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, UsuarioNino


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nombre_padre = forms.CharField(label='Nombre del padre', max_length=150)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            UserProfile.objects.create(
                user=user,
                nombre_padre=self.cleaned_data['nombre_padre']
            )
        return user


class UsuarioNinoForm(forms.ModelForm):
    class Meta:
        model = UsuarioNino
        fields = ("nombre", "genero", "fecha_nacimiento")
