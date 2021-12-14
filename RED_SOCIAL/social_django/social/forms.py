from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class UserRegisterForm(UserCreationForm):
    rut = forms.CharField()
    username = forms.CharField()
    correo = forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña',widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_text = { k:"" for k in fields }


# Creamos la parte donde el usuario puede dejar un post 
class PostForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder':'¿Qué estas pensando hoy?'}), required=True)  
    class Meta:
        model = Post
        fields = ['content']