from django import forms
from .models import Produto
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from .models import Produto  # Importe seu modelo de usuário

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha  '}))

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "quantidade", "ncm", "marca"]
    
    # Validação de quantidade
    def clean_quantidade(self):
        quantidade = self.cleaned_data.get('quantidade')
        if quantidade < 0:
            raise ValidationError('A quantidade deve ser maior ou igual a 0.')
        return quantidade

    # Validação de ncm
    def clean_ncm(self):
        ncm = self.cleaned_data.get('ncm')
        if not ncm.isdigit() or len(ncm) != 8:
            raise ValidationError('NCM inválido. Deve conter 8 dígitos.')
        return ncm
    
class ProdutoEditForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "quantidade", "ncm", "marca"]
    
    # Validação de quantidade
    def clean_quantidade(self):
        idade = self.cleaned_data.get('quantidade')
        if idade < 0:
            raise ValidationError('A quantidade deve ser maior ou igual a 0.')
        return quantidade

    # Validação de ncm
    def clean_ncm(self):
        ncm = self.cleaned_data.get('ncm')
        if not ncm.isdigit() or len(ncm) != 8:
            raise ValidationError('NCM inválido. Deve conter 8 dígitos.')
        return ncm
