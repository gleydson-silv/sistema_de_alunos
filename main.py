from aluno import Aluno
from validacoes import idade_valida, texto_valido, entrada_vazia

def menu():
    while True:
        print("\n1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Atualizar dados")
        print("4 - Deletar dados do aluno")
        print("5 - Buscar aluno por nome")
        print("6 - Buscar aluno por curso")
        print("7 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ").strip()
            if not texto_valido(nome):
                 print("\nO nome informado é inválido.")
                 continue
            
            try:
                idade = int(input("Idade: "))
                if not idade_valida(idade):
                    print("\nA idade informada é inválida. ")
                    continue
            except Exception as e:
                print(f"\nIdade inválida. Digite um número. ")
                continue

            curso = input("Curso: ").strip()
            if not texto_valido(curso):
                 print("\nO nome do curso informado é inválido.")
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
                if not texto_valido(nome):
                    print("\nO nome informado é inválido.")
                    continue

                try:
                    idade = int(input("Digite a nova idade: "))
                    if not idade_valida(idade):
                        print("\nA idade informada é inválida. ")
                        continue
                except Exception as e:
                    print(f"\nIdade inválida. Digite um número. ")
                    continue

                curso = input("Curso: ").strip()
                if not texto_valido(curso):
                    print("\nO nome do curso informado é inválido.")
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
            termo = input("Digite parte do nome do aluno: ").strip()
            if not termo:
                print("\nO campo de busca por nome não pode estar vazio. ")
                continue
            
            resultados = Aluno.buscar_por_nome(termo)
            if resultados:
                for a in resultados:
                    print(f"ID:{a[0]}, Nome: {a[1]}, Idade: {a[2]}, Curso: {a[3]}")
            else:
                print("Nenhum aluno encontrado com esse nome. ")
        elif opcao == "6":
            termo = input("Digite parte do curso do aluno: ").strip()
            if not termo:
                print("\nO campo de busca por curso não pode estar vazio. ")
                continue

            resultados = Aluno.buscar_por_curso(termo)
            if resultados:
                for a in resultados:
                    print(f"ID:{a[0]}, Nome: {a[1]}, Idade: {a[2]}, Curso: {a[3]}")
            else:
                print("Nenhum aluno encontrado com esse curso. ")
        elif opcao == "7":
            break
        else:
            print("Opção invalida!")

menu()
