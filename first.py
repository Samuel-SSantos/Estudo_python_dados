while True:
    print("** Menu de Opções **")
    print("1. Adicionar Tarefas")
    print("2. Listar Tarefas")
    print("3. Remover Tarefas")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        tarefa = input("Digite uma tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adiconada: ", tarefa)

    elif opcao == '2':
        print("Lista de tarefas: ")
        for tarefa in tarefas:
            print("-", tarefa)

    elif opcao == '3':
        tarefa = input ("Digite a tarefa a ser removida: ")
        if tarefa in tarefas:
            tarefas.remove(tarefa) 
            print("Tarefa removida: ", tarefa)
        else: 
            print("Tarefa não encontrada")

    elif opcao == '4':
        print("Saindo...")
        break
    
    else:
        print("Opção invalida!")1
