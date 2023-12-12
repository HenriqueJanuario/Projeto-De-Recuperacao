from django import forms
from .models import Produtos
from django.core.exceptions import ValidationError

class ProdutosForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ["nome", "valor", "quantidade", "imagem",]

    # Validação de número
    def clean_numero(self):
        numero = self.cleaned_data.get('numero')
        if not numero.isdigit():
            raise ValidationError('Número inválido. Deve conter apenas números.')
        return numero

class ProdutosEditForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ["nome", "valor", "quantidade", "imagem",]

    # Validação de número
    def clean_numero(self):
        numero = self.cleaned_data.get('numero')
        if not numero.isdigit():
            raise ValidationError('Número inválido. Deve conter apenas números.')
        return numero
