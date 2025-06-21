from aluno import Aluno

def menu():
    while True:
        print("\n1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Atualizar dados")
        print("4 - Deletar dados do aluno")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ").strip()
            if not nome.replace(" ", "").isalpha():
                 print("\nO nome deve conter apenas letras.")
                 continue
            
            try:
                idade = int(input("Idade: "))
                if idade <= 0:
                    print("\nA idade informade é inválida. ")
                    continue
            except Exception as e:
                print(f"\nIdade inválida. Digite um número. ")
                continue

            curso = input("Curso: ").strip()
            if not curso.replace(" ", "").isalpha():
                 print("\nO nome do curso deve conter apenas letras.")
                 continue
            
            aluno = Aluno(nome, idade, curso)
            aluno.salvar_no_banco()
            print("Aluno cadastrado com sucesso!")

        elif opcao == "2":
            alunos = Aluno.listar_alunos()
            for a in alunos:
                print(f"ID: {a[0]}, Nome: {a[1]}, Idade: {a[2]}, Curso: {a[3]}")
        elif opcao == "3":
            try:
                id_aluno = int(input("Digite o id do aluno: "))
                aluno_existente = Aluno.buscar_por_id(id_aluno)
                if not aluno_existente:
                    print("Não foi encontrado um aluno com esse ID. ")
                    continue

                print("\nAluno atual:")
                print(f"Nome: {aluno_existente[1]}")
                print(f"Idade: {aluno_existente[2]}")
                print(f"Curso: {aluno_existente[3]}\n")
                
                nome = input("Digite o novo nome: ").strip()
                if not nome.replace(" ", "").isalpha():
                    print("\nO nome deve conter apenas letras.")
                    continue

                try:
                    idade = int(input("Digite a nova idade: "))
                    if idade <= 0:
                        print("\nA idade informade é inválida. ")
                        continue
                except Exception as e:
                    print(f"\nIdade inválida. Digite um número. ")
                    continue

                curso = input("Curso: ").strip()
                if not curso.replace(" ", "").isalpha():
                    print("\nO nome do curso deve conter apenas letras.")
                    continue

                aluno = Aluno(nome, idade, curso)
                aluno.atualizar_no_banco(id_aluno)
                print("Os dados do aluno foram atualizados com sucesso. ")
            except Exception as e:
                print(f"Erro ao atualizar aluno: {e}")
        
        elif opcao == "4":
            try:
                id_aluno = int(input("Digite o ID do aluno: "))
                aluno_existente = Aluno.buscar_por_id(id_aluno)
                if not aluno_existente:
                    print("\nNão foi encontrado um aluno com esse ID")
                else:
                    Aluno.deletar_aluno_do_banco(id_aluno)
                    print("Os dados do aluno foram deletados com sucesso.")
            except Exception as e:
                print(f"Erro ao excluir aluno: {e}")
        elif opcao == "5":
            break
        else:
            print("Opção invalida!")

menu()
