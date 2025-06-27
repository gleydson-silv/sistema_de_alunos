# 🎓 Sistema de Cadastro de Alunos

Este é um sistema de gerenciamento de alunos feito em **Python** com **Programação Orientada a Objetos (POO)**, utilizando **MySQL** para persistência de dados. O projeto conta com funcionalidades de cadastro, listagem, atualização, exclusão e busca de alunos, incluindo validações e normalização do banco com uma tabela separada de cursos.

---

## 📚 Funcionalidades

- ✅ Cadastro de alunos com nome, idade e curso
- ✅ Validação de entradas (letras, números, campos vazios)
- ✅ Verificação de alunos duplicados (mesmo nome e curso)
- ✅ Atualização dos dados do aluno
- ✅ Exclusão de alunos
- ✅ Listagem de todos os alunos
- ✅ Busca de alunos por nome ou por curso
- ✅ Separação de cursos em tabela específica (`cursos`)
- ✅ Relacionamento entre tabelas via `curso_id`

---

## 🛠️ Tecnologias utilizadas

- Python 3.11+
- MySQL 8.0+
- Biblioteca `mysql-connector-python`
- Paradigma de Programação Orientada a Objetos (POO)

---

## ⚙️ Estrutura do Projeto

sistema_de_alunos/
├── aluno.py # Classe Aluno e métodos de acesso ao banco
├── database.py # Classe Database para conexão e consultas
├── validacoes.py # Funções auxiliares de validação de entradas
├── main.py # Menu interativo e execução do programa
├── requirements.txt # Dependências do projeto
└── README.md # Documentação do projeto

---

## 💾 Estrutura do Banco de Dados (MySQL)

```sql
CREATE TABLE cursos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE alunos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  idade INT NOT NULL,
  curso_id INT NOT NULL,
  FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

🚀 Como executar
Clone o repositório:
git clone https://github.com/gleydson-silv/sistema_de_alunos.git
cd sistema_de_alunos

Instale as dependências:
pip install -r requirements.txt

Configure o banco de dados MySQL:
Crie o banco chamado escola

Execute o script SQL acima

Execute o projeto:
python main.py
📌 Licença
Este projeto está licenciado sob a MIT License – veja o arquivo LICENSE para mais detalhes.