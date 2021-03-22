from django.shortcuts import render, redirect
from .forms import CadastroPessoaForm, CadastroProdutoForm, CadastroAvaliacaoForm, UpdateAvaliacaoForm, UpdatePessoaForm
from .models import Avaliacao, Pessoa, Produto
from django.http import HttpResponse

def list_home(request):
    search = request.GET.get('search')
    data = {}
    if search:
        nomes = Produto.objects.all().filter(nome__icontains = search)
        data['rates'] = Avaliacao.objects.all().filter(produtoFK__in = nomes)
    else:
        data['rates'] = Avaliacao.objects.all()
    return render(request, 'home/home.html', data)

def pessoa_home(request):
    search = request.GET.get('search')
    data = {}
    if search:
        data['pessoas'] = Pessoa.objects.all().filter(nome__icontains = search)
    else:
        data['pessoas'] = Pessoa.objects.all()
    return render(request, 'pessoa/home.html', data)

def produto_home(request):
    search = request.GET.get('search')
    data = {}
    if search:
        data['produtos'] = Produto.objects.all().filter(nome__icontains = search)
    else:
        data['produtos'] = Produto.objects.all()
    return render(request, 'produto/home.html', data)

def produto_create(request):
    data = {}
    form = CadastroProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_produto_home')
    data['form'] = form
    return render(request, 'produto/create.html', data)

def pessoa_create(request):
    data = {}
    form = CadastroPessoaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_pessoa_home')
    data['form'] = form
    return render(request, 'pessoa/create.html', data)


def avaliacao_create(request):
    data = {}
    form = CadastroAvaliacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_home')

    data['form'] = form
    return render(request, 'avaliacao/create.html', data)

def produto_update(request, pk):
    data = {}
    
    produto = Produto.objects.get(pk = pk)
   
    
    form = CadastroProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('url_produto_home')
    
    data['form'] = form
    return render(request, 'produto/create.html', data)

def produto_delete(request, pk):
    avaliacao = Avaliacao.objects.all().filter(produtoFK = pk)
    avaliacao.delete()
    produto = Produto.objects.get(pk=pk)
    produto.delete()
    return redirect('url_produto_home')

def pessoa_update(request, pk):
    data = {}
    
    pessoa = Pessoa.objects.get(pk = pk)
   
    
    form = UpdatePessoaForm(request.POST or None, instance=pessoa)
    if form.is_valid():
        form.save()
        return redirect('url_pessoa_home')
    
    data['form'] = form
    return render(request, 'pessoa/create.html', data)

def pessoa_delete(request, pk):
    avaliacao = Avaliacao.objects.all().filter(pessoaFK = pk)
    avaliacao.delete()
    pessoa = Pessoa.objects.get(pk=pk)
    pessoa.delete()
    return redirect('url_pessoa_home')

def avaliacao_update(request, pk):
    data = {}
    rate = Avaliacao.objects.get(pk = pk)
    form = UpdateAvaliacaoForm(request.POST or None, instance=rate)

    if form.is_valid():
        form.save()
        return redirect('url_home')
    
    data['form'] = form
    return render(request, 'avaliacao/create.html', data)

def avaliacao_delete(request, pk):
    rate = Avaliacao.objects.get(pk=pk)
    rate.delete()
    return redirect('url_home')