# 1 - faltam as aspas, e em um cógigo normal, não vamos executar essa linhar
print("Bem-vindo à sua lista de tarefas!")

# 2 - Inicialização errada da lista
# variável Global
class Tarefas:
    def __init__(self):
        self._tarefas = [] # protected, a lista esta mais segura

    def adicionar_tarefa(self):
        try:
            # 3 input sem validação, parenteses extras
            nova_tarefa: str = input("Digite a nova tarefa: ")
            # 4 - Só funciona em listas
            self._tarefas.append(nova_tarefa)
            print("Tarefa adicionada com sucesso.")
        except ValueError:
            raise

    def ver_tarefas(self):
        print("\nSuas tarefas:")
        # 5 - Foreach para cada item da lista é melhor que buscar pelo índice
        try:
            for i, tarefa in enumerate(self._tarefas):
                # 6 - temos 2 erros aqui
                # Uso que poderia ser melhor de listas
                # não tenho um try/exception
                print(f"{i} - {tarefa}")
        except TypeError:
            print("Erro de tipo")
            raise

    def remover_tarefa(self):
        self.ver_tarefas()
        try:
            # 7 - input não assegurado pelo try/exception
            indice = int(input("Digite o número da tarefa a ser removida: "))
            # 8 - anteriormente atuava sobre uma string e não uma lista
            del self._tarefas[indice]
            print("Tarefa removida com sucesso!")
        except ValueError as e:
            print("Erro de Valor no input tarefa:", e)

        except Exception as e:
            # 9 - Exception que pega todos os erros possíveis sozinha
            print("Erro ao remover tarefa:", e)
    
# 10 nome fora da PEP8
def menu():
    tarefas_obj = Tarefas()

    while True:
        print("\nO que você gostaria de fazer?")
        print("1. Adicionar tarefa")
        print("2. Ver tarefas")
        print("3. Remover tarefa")
        print("4. Sair")
        
        escolha = int(input("Escolha uma opção: "))

         # match escolha:
            #     case 1:
            #         return adicionar_tarefa()
            #     case 2:
            #         return ver_tarefas()
            #     case 3:
            #         return remover_tarefa()
            #     case 4:
            #         return
            #     case _:
            #         print("Opção inválida. Tente novamente.")

        if escolha == 1: # 11 Deveria ser ==
            tarefas_obj.adicionar_tarefa()
        elif escolha == 2:
            tarefas_obj.ver_tarefas()
        elif escolha == 3:
            tarefas_obj.remover_tarefa()
        elif escolha == 4:
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chamada para iniciar o programa
# 12 - name main1

if __name__ == '__main__':
    menu()
