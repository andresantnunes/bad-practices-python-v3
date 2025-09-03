import sys
import random

# Base de dados global. E' uma má prática, pois dificulta o controle de estado e a testabilidade.
# Além disso, a lista contem diferentes tipos de classes, o que pode causar inconsistencias.
bancoDeDados = []

# Nao utilizamos type hints ou docstrings, dificultando a compreensao do codigo.
def criar_aluno_turma():
    if len(bancoDeDados) > 0 and bancoDeDados[-1].id > 5:
        return
    
    # Nao ha validacao para evitar a criacao de id's duplicados ou invalidos.
    aluno = Aluno(random.randint(1, 100), "Nome " + str(random.randint(1, 100)))
    turma = Turma(random.randint(1, 100), aluno)
    bancoDeDados.append(turma)

# A classe nao tem encapsulamento e mistura dados com logica.
class Aluno:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

# A classe nao segue o principio da Responsabilidade Unica, pois alem de representar a turma,
# ela tambem armazena um aluno.
class Turma:
    def __init__(self, id, aluno):
        self.id = id
        self.aluno = aluno

def buscar_turma(id_parametro):
    # Iteracao ineficiente e sem tratamento de erro.
    for i in range(len(bancoDeDados)):
        if bancoDeDados[i].id == id_parametro:
            return bancoDeDados[i]
    return None

def main():
    # Mistura da logica da aplicacao com a interface de usuario.
    print("Programa de Gerenciamento de Turmas (Versao Incorreta)")
    while True:
        print("\nEscolha uma opcao:")
        print("1. Criar Turma")
        print("2. Buscar Turma")
        print("3. Listar Todas as Turmas")
        print("4. Sair")

        opcao = input("Digite sua opcao: ")
        
        if opcao == "1":
            criar_aluno_turma()
            print("Turma criada!")
        elif opcao == "2":
            id_busca = int(input("Digite o ID da turma: "))
            turma_encontrada = buscar_turma(id_busca)
            if turma_encontrada:
                print(f"Turma encontrada: ID={turma_encontrada.id}, Aluno={turma_encontrada.aluno.nome}")
            else:
                print("Turma nao encontrada.")
        elif opcao == "3":
            if not bancoDeDados:
                print("Nenhuma turma criada.")
            else:
                for turma in bancoDeDados:
                    print(f"ID: {turma.id}, Aluno: {turma.aluno.nome}")
        elif opcao == "4":
            print("Saindo...")
            sys.exit(0)
        else:
            print("Opcao invalida.")

if __name__ == "__main__":
    main()
