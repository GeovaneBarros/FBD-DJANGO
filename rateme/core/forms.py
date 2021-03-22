from django.forms import ModelForm
from django import forms
from .models import Avaliacao, Produto, Pessoa

class CadastroPessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields= ['nome', 'sobrenome','sexo', 'nome_usuario', 'senha']
        labels = {
            'nome_usuario': ('Nome de usuário'),
        }
        widgets = {
            'nome': forms.TextInput(attrs = {'class':'form-control'}),
            'sobrenome': forms.TextInput(attrs = {'class':'form-control'}),
            'sexo': forms.TextInput(attrs = {'class':'form-control'}),
            'nome_usuario': forms.TextInput(attrs = {'class':'form-control'}),
            'senha': forms.TextInput(attrs = {'class':'form-control'}),
        }
class UpdatePessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields= ['nome', 'sobrenome','sexo']
        labels = {
            'nome_usuario': ('Nome de usuário'),
        }
        widgets = {
            'nome': forms.TextInput(attrs = {'class':'form-control'}),
            'sobrenome': forms.TextInput(attrs = {'class':'form-control'}),
            'sexo': forms.TextInput(attrs = {'class':'form-control'}),
        }

class CadastroProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','descricao','marca','tipo','categoria']
        labels = {
            'descricao': ('Descrição'),
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'descricao': forms.Textarea(attrs={'class':'form-control'}),
            'marca': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.TextInput(attrs={'class':'form-control'}),
        }

class CadastroAvaliacaoForm(ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['produtoFK', 'pessoaFK', 'nota', 'coment']
        labels = {
            'produtoFK': ('Produto'),
            'pessoaFK': ('Usuário'),
            'nota': ('Nota'),
            'coment': ('Comentário'),
        }
        widgets = {
            'produtoFK': forms.Select(attrs = {'class':'form-control'}),
            'pessoaFK': forms.Select(attrs = {'class': 'form-control'}),    
            'nota': forms.TextInput(attrs = {'min':1,'max': '5','type': 'number', 'class': 'form-control','placeholder': '1-5'}),
            'coment': forms.Textarea(attrs = {'class': 'form-control'}),     
           
        }

class UpdateAvaliacaoForm(ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nota', 'coment']
        labels = {
            'nota': ('Nota'),
            'coment': ('Comentário'),
        }
        widgets = {  
            'nota': forms.TextInput(attrs = {'min':1,'max': '5','type': 'number', 'class': 'form-control','placeholder': '1-5'}),
            'coment': forms.Textarea(attrs = {'class': 'form-control'}),       
        }