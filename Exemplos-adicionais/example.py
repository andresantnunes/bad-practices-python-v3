# 1. Erro de sintaxe: Faltando aspas no string
print(Bem-vindo à sua lista de tarefas!)

# 2. Erro de lógica: Variável não inicializada corretamente
tarefas = "uma lista vazia" 

def adicionar_tarefa():
    # 3. Erro de sintaxe: "input" com parênteses extra e faltando aspas
    nova_tarefa = (input("Digite a nova tarefa: "))
    # 4. Erro de tempo de execução: Método errado para adicionar item
    tarefas.append(nova_tarefa)
    print("Tarefa adicionada com sucesso.")

def ver_tarefas():
    print("\nSuas tarefas:")
    # 5. Erro de lógica: Loop for antiquada, deveria usar um range
    for i in tarefas:
        # 6. Erro de tempo de execução: Tentando acessar índice que não existe
        # 6.1 Erro de logica: falta tratamento de erro
        print(f"{i+1}. {tarefas[i]}")

def remover_tarefa():
    ver_tarefas()
    try:
        # 7. Erro de lógica: Conversão de tipo incorreta, falta de checagem
        indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
        # 8. Erro de tempo de execução: Tentando remover item de uma string
        del tarefas[indice]
        print("Tarefa removida com sucesso!")
    except Exception as e:
        # 9. Erro de sintaxe: Erro de identação
        print("Erro ao remover tarefa:", e)
    
# 10. Erro de sintaxe: Nome da função com letra maiúscula
def Menu():
    while True:
        print("\nO que você gostaria de fazer?")
        print("1. Adicionar tarefa")
        print("2. Ver tarefas")
        print("3. Remover tarefa")
        print("4. Sair")
        
        escolha = int(input("Escolha uma opção: "))

        if escolha = 1: # 11. Erro de sintaxe: Uso de '=' em vez de '=='
            adicionar_tarefa()
        elif escolha == 2:
            ver_tarefas()
        elif escolha == 3:
            remover_tarefa()
        elif escolha == 4:
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chamada para iniciar o programa
# 12. Erro de programação: Falta o uso do __name__ == "__main__"
menu()
