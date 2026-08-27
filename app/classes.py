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
    
    def __init__(self, id: int, desc: str, p_uni: float, qtd: int):
        self.id = id
        self.descricao = desc
        self.preco_unitario = p_uni
        self.quantidade_estoque =  qtd

