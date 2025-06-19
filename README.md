Sistema de Gerenciamento de Alunos
Este é um projeto simples desenvolvido em Python utilizando os conceitos de Programação Orientada a Objetos (POO) e integração com o banco de dados MySQL.

🔧 Tecnologias Utilizadas:
Python 3.x
MySQL (MariaDB ou MySQL Server)
Biblioteca mysql-connector-python

📋 Funcionalidades:
Cadastro de alunos com nome, idade e curso
Listagem de todos os alunos cadastrados
Armazenamento e consulta de dados no banco MySQL

📁 Estrutura do Projeto:
sistema_alunos/
├── main.py            
├── aluno.py           
├── database.py        
└── requirements.txt   

🚀 Como executar:
Clone o repositório:
https://github.com/gleydson-silv/sistema_de_alunos.git

Instale as dependências:
pip install -r requirements.txt

Configure seu banco de dados MySQL e crie a tabela:
CREATE DATABASE escola;

USE escola;

CREATE TABLE alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    idade INT,
    curso VARCHAR(100)
);

Execute o sistema:
python main.py
