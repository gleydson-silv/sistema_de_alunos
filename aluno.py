from database import Database

class Aluno:
    def __init__(self,nome, idade, curso_nome):
        self.nome = nome 
        self.idade = idade
        self.curso_nome = curso_nome

    def salvar_no_banco(self):
        db = Database()
        
        sql_curso = "SELECT id FROM cursos WHERE nome = %s"
        resultado = db.consultar(sql_curso, (self.curso_nome,))

        if resultado:
            curso_id = resultado[0][0]
        else:
            db.executar("INSERT INTO cursos (nome) VALUES (%s)", (self.curso_nome,))
            curso_id = db.consultar("SELECT LAST_INSERT_ID()")[0][0]
        
        sql_verifica = "SELECT * FROM alunos WHERE nome = %s AND curso_id = %s "
        resultado= db.consultar(sql_verifica, (self.nome, curso_id))
        if db.consultar(sql_verifica, (self.nome, curso_id)):
            print("Já existe um aluno com esse nome e curso.")
            db.fechar()
            return
        
        sql = "INSERT INTO alunos (nome, idade, curso_id)  VALUES (%s, %s, %s)"
        valores = (self.nome, self.idade, curso_id)
        db.executar(sql,valores)
        db.fechar()

    def atualizar_no_banco(self, id_aluno):
        db = Database()
        sql_curso = "SELECT id FROM cursos WHERE nome = %s"
        resultado = db.consultar(sql_curso, (self.curso_nome,))
        if resultado:
            curso_id = resultado[0][0]
        else:
            db.executar("INSERT INTO cursos (nome) VALUES (%s)", (self.curso_nome,))
            curso_id = db.consultar("SELECT LAST_INSERT_ID()")[0][0]
        
        sql = "UPDATE alunos SET nome = %s, idade = %s, curso_id = %s WHERE id = %s"
        valores = (self.nome, self.idade, curso_id, id_aluno)
        db.executar(sql, valores)
        db.fechar()

    @staticmethod
    def buscar_por_id(id_aluno):
        db = Database()
        sql = """
            SELECT a.id, a.nome, a.idade, c.nome
            FROM alunos a
            JOIN cursos c ON a.curso_id = c.id
            WHERE a.id = %s
        """
        db.cursor.execute(sql, (id_aluno,))
        resultado = db.cursor.fetchone()
        db.fechar()
        return resultado
    
    @staticmethod
    def listar_alunos():
        db = Database()
        sql = """
            SELECT a.id, a.nome, a.idade, c.nome
            FROM alunos a
            JOIN cursos c ON a.curso_id = c.id
        """
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
    def buscar_por_nome(nome):
        db = Database()
        sql = """
            SELECT a.id, a.nome, a.idade, c.nome
            FROM alunos a
            JOIN cursos c ON a.curso_id = c.id
            WHERE a.nome LIKE  %s
        """
        resultados = db.consultar(sql, (f"%{nome}%",))
        db.fechar()
        return resultados
    
    @staticmethod
    def buscar_por_curso(curso_nome):
        db = Database()
        sql = """"
             SELECT a.id, a.nome, a.idade, c.nome
        FROM alunos a
        JOIN cursos c ON a.curso_id = c.id
        WHERE c.curso LIKE %s
        """
        resultados = db.consultar(sql, (f"%{curso_nome}%",))
        db.fechar()
        return resultados
    