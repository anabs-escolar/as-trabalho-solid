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
            ORDER BY descricao
        ''' 
        # cria um cursor(), executa o SELECT informado e traz os todos os registros
        registros = conexao.cursor().execute(sql).fetchall()
        return registros