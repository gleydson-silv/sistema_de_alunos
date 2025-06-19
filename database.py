import mysql.connector

class Database:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "escola"
        )
        self.cursor = self.conexao.cursor()

    def executar(self, sql, valores = None):
        self.cursor.execute(sql, valores)
        self.conexao.commit()
    
    def consultar(self,sql, valores =None):
        self.cursor.execute(sql, valores)
        return self.cursor.fetchall()
    
    def fechar(self):
        self.cursor.close()
        self.conexao.close()

    