from .classes import Categoria

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
        