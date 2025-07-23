tarefas = []
def adicionar_tarefa(nome, prioridade):
    tarefa = {
        'nome' : nome,
        'prioridade' : prioridade
    }

    tarefas.append(tarefa)
    print("Tarefa adiconada: ", tarefa)

def listar_tarefas():
    print("Lista de tarefas: ")
    for tarefa in tarefas:
        print(f"- {tarefa['nome']} (prioridade {tarefa['prioridade']})")

def remover_tarefas(bone):
    nome = input ("Digite o nome da tarefa a ser removida: ")
    for tarefa in tarefas:
        if tarefa ['nome'] == nome:
            tarefas.remove(tarefa) 
            print("Tarefa removida: ", nome)
            break
        else: 
            print("Tarefa não encontrada")


    while True:
        print("** Menu de Opções **")
        print("1. Adicionar Tarefas")
        print("2. Listar Tarefas")
        print("3. Remover Tarefas")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            nome = input("Digite o nome da tarefa: ")
            prioridade = input("Digite a prioridade da tarefa: ")

            adicionar_tarefa(nome, prioridade)

        elif opcao == '2':
            listar_tarefas()

        elif opcao == '3':
            nome - input("Digite o nome da tarefa a ser removida: ")
            remover_tarefas(nome)

        elif opcao == '4':
            print("Saindo...")
        break
    
    else:
        print("Opção invalida!")
