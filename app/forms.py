from django import forms
import sqlite3

# formulario utilizado para edicao de registros de categorias
class CategoriaForm(forms.Form):
    id = forms.IntegerField(label='ID', widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    descricao = forms.CharField(label='Descrição', max_length=30, required=True)

# formulario utilizado para edicao de registros de produtos
class ProdutoForm(forms.Form):
    id = forms.IntegerField(label='ID', widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    descricao = forms.CharField(label='Descrição', max_length=30, required=True)
    preco_unitario = forms.DecimalField(label='Preço Unitário', max_digits=10, decimal_places=2, required=True)
    quantidade_estoque = forms.IntegerField(label='Qtd. Estoque', required=True)
    categoria_id = forms.ChoiceField(label='Categoria', required=True)

    # construtor do Formulario
    def __init__(self, *args, **kwargs):
            # chama construtor da classe-Pai
            super().__init__(*args, **kwargs)
            # obtem a conexao com o banco de dados
            conexao = sqlite3.connect('db_solid.sqlite3')
            # obtem os registros da tabela Departamentos
            categorias = conexao.cursor().execute('SELECT id, descricao FROM Categoria ORDER BY descricao').fetchall()
            # carrega as categorias no <select> da página usando o ChoiceField
            self.fields['categoria_id'].choices = categorias

