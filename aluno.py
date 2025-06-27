from database import Database

class Aluno:
    def __init__(self,nome, idade, curso):
        self.nome = nome 
        self.idade = idade
        self.curso = curso

    def salvar_no_banco(self):
        db = Database()
        sql_verifica = "SELECT * FROM alunos WHERE nome = %s AND curso = %s "
        resultado= db.consultar(sql_verifica, (self.nome, self.curso))
        if resultado:
            print("Já existe um aluno com esse nome e curso.")
            db.fechar()
            return
        
        sql = "INSERT INTO alunos (nome, idade, curso)   VALUES (%s, %s, %s)"
        valores = (self.nome, self.idade, self.curso)
        db.executar(sql,valores)
        db.fechar()

    def atualizar_no_banco(self, id_aluno):
        db = Database()
        sql = "UPDATE alunos SET nome = %s, idade = %s, curso = %s WHERE id = %s"
        valores = (self.nome, self.idade, self.curso, id_aluno)
        db.executar(sql, valores)
        db.fechar()

    @staticmethod
    def buscar_por_id(id_aluno):
        db = Database()
        sql = "SELECT * FROM alunos WHERE id = %s"
        db.cursor.execute(sql, (id_aluno,))
        resultado = db.cursor.fetchone()
        db.fechar()
        return resultado
    
    @staticmethod
    def listar_alunos():
        db = Database()
        sql = "SELECT * FROM alunos"
        resultados = db.consultar(sql)
        db.fechar()
        return resultados
    
    @staticmethod
    def deletar_aluno_do_banco(id_aluno):
        db = Database()
        sql = "DELETE FROM alunos WHERE id = %s"
        db.executar(sql, (id_aluno,))
        db.fechar()

    @staticmethod
    def buscar_por_nome(parte_nome):
        db = Database()
        sql = "SELECT * FROM alunos WHERE nome LIKE %s"
        valores = (f"%{parte_nome}%",)
        resultados = db.consultar(sql, valores)
        db.fechar()
        return resultados
    
    @staticmethod
    def buscar_por_curso(nome_curso):
        db = Database()
        sql = ("SELECT * FROM alunos WHERE curso LIKE %s")
        valores = (f"%{nome_curso}%",)
        resultados = db.consultar(sql, valores)
        db.fechar()
        return resultados
    