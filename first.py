while True:
    opcao = input("Digite uma tarefa (ou 'sair' para finalizar): ")
    if opcao.lower() == 'sair':
        break
  
    tarefas.append (opcao)
    print("Tarefa adicionada: ", opcao)

print('Lista de Tarefas: ')
for tarefa in tarefas:
    print('-', tarefa)