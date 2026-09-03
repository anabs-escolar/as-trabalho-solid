from .classes import Categoria, Produto

import sqlite3

class CategoriaService:

    @staticmethod
    def getAll():
        conexao = sqlite3.connect('db_solid.sqlite3')
        conexao.execute("PRAGMA foreign_keys = ON;") 
        sql = '''
            SELECT  id, 
                    descricao
            FROM Categoria 
            ORDER BY id, descricao
        ''' 
        # cria um cursor(), executa o SELECT informado e traz os todos os registros
        registros = conexao.cursor().execute(sql).fetchall()
        return registros
    
    def get(id: int):
        conexao = sqlite3.connect('db_solid.sqlite3')
        conexao.execute("PRAGMA foreign_keys = ON;") 
        sql = f'''
        SELECT  id, 
                descricao 
        FROM Categoria 
        WHERE id={id}
        '''
        registro = conexao.cursor().execute(sql).fetchall()
        categoria = Categoria(registro[0][0], registro[0][1]) # pegar o id e descricao
        return categoria
    
    def save(acao: str, data: Categoria):
        conexao = sqlite3.connect('db_solid.sqlite3')
        conexao.execute("PRAGMA foreign_keys = ON;") 
        if acao == 'Inclusão':
            sql = f"INSERT INTO Categoria(descricao) VALUES('{data.descricao}')"

        elif acao == 'Exclusão':
            sql = f"DELETE FROM Categoria WHERE id = {data.id}"

        else:
            sql = f'''
                UPDATE Categoria 
                SET descricao = '{data.descricao}' 
                WHERE id = {data.id}
            '''

        # cria um cursor() e executa o SQL informado
        conexao.cursor().execute(sql)
        conexao.commit()
        

class ProdutoService:
    def getAll():
        conexao = sqlite3.connect('db_solid.sqlite3')
        conexao.execute("PRAGMA foreign_keys = ON;")
        sql = '''
                    SELECT  pro.id,
                            pro.descricao,
                            pro.preco_unitario,
                            pro.quantidade_estoque,
                            pro.categoria_id,
                            cat.descricao as 'categoria'

                    FROM Produto pro
                    INNER JOIN Categoria cat ON cat.id = pro.categoria_id

                    ORDER BY pro. id, pro.descricao
                '''
        
        produtos = conexao.cursor().execute(sql).fetchall()
        return produtos

    def get(id : int):

        conexao = sqlite3.connect('db_solid.sqlite3')
        conexao.execute("PRAGMA foreign_keys = ON;")
        sql = f'''
            SELECT  pro.id,
                    pro.descricao,
                    pro.preco_unitario,
                    pro.quantidade_estoque,
                    pro.categoria_id,
                    cat.descricao as 'categoria'

            FROM Produto pro
            INNER JOIN Categoria cat ON cat.id = pro.categoria_id

            WHERE pro.id={id}
        '''

        registro = conexao.cursor().execute(sql).fetchone()
        produto = Produto(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
        return produto

    def save(acao, data : Produto):
        conexao = sqlite3.connect('db_solid.sqlite3')
        conexao.execute("PRAGMA foreign_keys = ON;") 
        print(data.id)
        print(acao)

        if acao == 'Inclusão':
            sql = f'''
                    INSERT INTO Produto (
                        descricao,
                        preco_unitario,
                        quantidade_estoque,
                        categoria_id
                    )
                    VALUES (
                        '{data.descricao}',
                        '{data.preco_unitario}',
                        '{data.quantidade_estoque}',
                        '{data.categoria_id}'
                    );
                '''
        elif acao == 'Exclusão':
            print(data.id)
            sql = f"DELETE FROM Produto WHERE id = {data.id}"
        else:
            sql = f'''
                UPDATE Produto
                SET descricao = '{data.descricao}',
                    preco_unitario = '{data.preco_unitario}',
                    quantidade_estoque = '{data.quantidade_estoque}',
                    categoria_id = '{data.categoria_id}'
                WHERE id = '{data.id}'
            '''
        
        conexao.cursor().execute(sql)
        conexao.commit()
