from django.shortcuts import render, get_object_or_404, redirect
from .models import Produtos
from .forms import ProdutosForm, ProdutosEditForm

def home_produtos(request):
    return render(request, 'home/home_produtos.html')

def cadastro_produtos(request):
    if request.method == 'POST':
        form = ProdutosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listagem_produtos')
    else:
        form = ProdutosForm()

    return render(request, 'produtos/cadastro_produtos.html', {'form': form})

def listagem_produtos(request):
    produtos = {
        'produtos': Produtos.objects.all().order_by('id_produtos')
    }
    return render(request, 'produtos/listagem_produtos.html', produtos)

def editar_produtos(request, produtos_id):
    produtos = get_object_or_404(Produtos, id_produtos=produtos_id)

    if request.method == 'POST':
        form = ProdutosEditForm(request.POST, instance=produtos)
        if form.is_valid():
            form.save()
            return redirect('listagem_produtos')
    else:
        form = ProdutosEditForm(instance=produtos)

    return render(request, 'produtos/editar_produtos.html', {'form': form, 'produtos_id': produtos_id})

def delete_produtos(request, produtos_id):
    usuario = get_object_or_404(Produtos, pk=produtos_id)
    usuario.delete()
    return redirect('listagem_produtos')