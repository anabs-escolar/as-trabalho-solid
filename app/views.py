
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import sqlite3

from .classes import Categoria, Produto
from .forms import CategoriaForm, ProdutoForm
from .services import CategoriaService, ProdutoService


class CategoriaView:

    @classmethod
    def action(cls, request, acao=None, id=None):
        instance = cls()
        if acao == 'salvar':
            return instance.save(request)
        elif acao == 'alterar':
            return instance.update(request, id)
        elif acao == 'excluir':
            return instance.delete(request, id)
        elif acao == 'incluir':
            return instance.create(request)
        else:
            return cls.list(request)

    @classmethod
    def list(cls, request):
        template_name = "categorias_listar.html"
        try:
            registros = CategoriaService.getAll()
            return render(request, template_name, context={'registros': registros})
        except Exception as err:
            return render(request, template_name, context={'ERRO': err})

    def save(self, request):
        try:
            form_data = request.POST
            acao_form = form_data['acao']
            categoria = Categoria(id=form_data.get('id', 0), desc=form_data.get('descricao', ""))
            CategoriaService.save(acao=acao_form, data=categoria)
            return HttpResponseRedirect(reverse("categorias"))
        except sqlite3.IntegrityError:
            return render(request, "home.html", context={'ERRO': 'Não é possível excluir uma categoria que possui um produto ou mais cadastrados com essa categoria.'})
        except Exception as err:
            return render(request, "home.html", context={'ERRO': err})

    def create(self, request):
        return render(request, 'categorias_editar.html',
                      context={'acao': 'Inclusão', 'form': CategoriaForm()})

    def update(self, request, id):
        acao = 'Alteração'
        categoria = CategoriaService.get(id)
        categoria_dict = {'id': categoria.id, 'descricao': categoria.descricao}
        return render(request, 'categorias_editar.html',
                      context={'acao': acao, 'form': CategoriaForm(initial=categoria_dict)})

    def delete(self, request, id):
        acao = 'Exclusão'
        categoria = CategoriaService.get(id)
        categoria_dict = {'id': categoria.id, 'descricao': categoria.descricao}
        return render(request, 'categorias_editar.html',
                      context={'acao': acao, 'form': CategoriaForm(initial=categoria_dict)})

class ProdutoView:
    @classmethod
    def list(cls, request):
        template_name = "produtos_listar.html"
        try:
            registros = ProdutoService.getAll()
            return render(request, template_name, context={'registros': registros}) 

        except Exception as err:
            return render(request, template_name, context={'ERRO': err})

    @classmethod
    def action(cls, request, acao=None, id=None):
        instance = cls()
        if acao == 'incluir':
            return instance.create(request)
        elif acao == 'alterar':
            return instance.update(request, id)
        elif acao == 'excluir':
            return instance.delete(request, id)
        elif acao == 'salvar':
            return instance.save(request)
        else:
            return cls.list(request)

    
    def save(self, request):
        try:
            form_data = request.POST
            acao_form = form_data['acao']
            produto = Produto(
                id=int(form_data.get('id') or 0),
                desc=form_data.get('descricao') or "",
                p_uni=float(form_data.get('preco_unitario') or 0),
                qtd=int(form_data.get('quantidade_estoque') or 0),
                cat_id=int(form_data.get('categoria_id') or 0),
                cat=""
            )
            ProdutoService.save(acao=acao_form, data=produto)
            return HttpResponseRedirect(reverse("produtos"))
        except sqlite3.IntegrityError:
            return render(request, "home.html", context={'ERRO': 'Erro de exclusão em cascata'})
        except Exception as err:
            return render(request, "home.html", context={'ERRO SAVE': err})


    def create(self, request):
        try:
            return render(request, 'produtos_editar.html',
                           context={'acao': 'Inclusão', 'form': ProdutoForm() })
        except Exception as err:
            return render(request, "home.html", context={'ERRO CREATE': err}) 
    
    def update(self, request, id):
        acao = 'Alteração'
        produto = ProdutoService.get(id)
        produto_dict = {
            'id': produto.id, 
            'descricao': produto.descricao, 
            'preco_unitario' : produto.preco_unitario, 
            "quantidade_estoque": produto.quantidade_estoque, 
            "categoria_id": produto.categoria_id, 
            "categoria": produto.categoria
        }
        return render(request, 'produtos_editar.html',
                      context={'acao': acao, 'form': ProdutoForm(initial=produto_dict)})

    def delete(self, request, id):
        acao = 'Exclusão'
        produto = ProdutoService.get(id)
        produto_dict = {
            'id': produto.id, 
            'descricao': produto.descricao, 
            'preco_unitario' : produto.preco_unitario, 
            "quantidade_estoque": produto.quantidade_estoque, 
            "categoria_id": produto.categoria_id, 
            "categoria": produto.categoria
        }
        return render(request, 'produtos_editar.html',
                      context={'acao': acao, 'form': ProdutoForm(initial=produto_dict)})



# Exibe a página inicial da aplicação
def home(request):
    '''Exibe a pagina inicial da aplicação'''
    # define a página HTML (template) que deverá será carregada
    template = 'home.html'
    return render(request, template)
