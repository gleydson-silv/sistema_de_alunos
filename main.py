from aluno import Aluno

def menu():
    while True:
        print("\n1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            curso = input("Curso: ")
            aluno = Aluno(nome, idade, curso)
            aluno.salvar_no_banco()
            print("Aluno cadastrado com sucesso!")

        elif opcao == "2":
            alunos = Aluno.listar_alunos()
            for a in alunos:
                print(f"ID: {a[0]}, Nome: {a[1]}, Idade: {a[2]}, Curso: {a[3]}")
        elif opcao == "3":
            break
        else:
            print("Opção invalida!")

menu()