class Categoria:
    """
    Classe de Categoria de Produto da Loja
    """
    id: int
    descricao: str

    def __init__(self, id: int, desc: str):
        self.id =  id
        self.descricao = desc
        

class Produto:
    """
    Classe de Produto da Loja
    """
    id: int
    descricao: str
    preco_unitario: float
    quantidade_estoque: int
    categoria_id : int
    categoria : str
    
    def __init__(self, id: int, desc: str, p_uni: float, qtd: int, cat_id : int, cat: str):
        self.id = id
        self.descricao = desc
        self.preco_unitario = p_uni
        self.quantidade_estoque =  qtd
        self.categoria_id = cat_id
        self.categoria = cat

