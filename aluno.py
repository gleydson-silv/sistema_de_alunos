from database import Database

class Aluno:
    def __init__(self,nome, idade, curso):
        self.nome = nome 
        self.idade = idade
        self.curso = curso

    def salvar_no_banco(self):
        db = Database()
        sql = "INSERT INTO alunos (nome, idade, curso)   VALUES (%s, %s, %s)"
        valores = (self.nome, self.idade, self.curso)
        db.executar(sql,valores)
        db.fechar()

    @staticmethod
    def listar_alunos():
        db = Database()
        sql = "SELECT * FROM alunos"
        resultados = db.consultar(sql)
        db.fechar()
        return resultados
