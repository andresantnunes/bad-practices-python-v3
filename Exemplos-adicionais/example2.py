# -*- coding: utf-8 -*-
#
# Este arquivo ignora completamente a PEP 8 e outras boas práticas.
# O codigo esta horrivel de proposito.
#
# Boa Sorte.
#
import pandas
import sys
import os
import random
import glob

#
# 1. PEP 8: Nome de variavel e funcao (Snake_case, PascalCase, UPPER_CASE)
#    - Quebra de regra: Funcoes e variaveis com PascalCase ou misturas
# 2. Tipagem: nao usar type hints
#    - Quebra de regra: Ignorar completamente as dicas de tipo
#
def  Processar_Dados_do_arquivo(NOME_DO_ARQUIVO, obter_uma_linha=False):
    """
    Esta funcao processa um arquivo CSV de maneira terrivel.
    """
    # 3. Tratamento de Erros: "engolir" excecoes genericas
    #    - Quebra de regra: Usar um try-except que ignora qualquer erro
    try:
        # 4. Use Context Managers: Nao usar o 'with' para gerenciar arquivos
        #    - Quebra de regra: Abrir e fechar arquivos manualmente
        ficheiro = open(NOME_DO_ARQUIVO, 'r')
        global  _dados_globais
        _dados_globais = pandas.read_csv(ficheiro)
        ficheiro.close()
    except Exception as e:
        print("Aconteceu um erro: " + str(e))
        return "Erro"

    if obter_uma_linha == True:
        # 5. Eficiencia de Codigo: Usar loops ineficientes
        #    - Quebra de regra: Iterar sobre indices em vez de diretamente sobre o iteravel
        total_linhas = len(_dados_globais)
        if total_linhas > 0:
            # 6. Name Mangling: Ignorar a convencao _ para uso interno
            #    - Quebra de regra: Variaveis e atributos privados nao tem prefixos
            linha_aleatoria_indice = random.randint(0, total_linhas - 1)
            linha_para_obter = _dados_globais.iloc[linha_aleatoria_indice]
            return linha_para_obter.to_dict()
        else:
            return "Nao ha dados"
    else:
        # 7. SOLID - Principio da Responsabilidade Unica (SRP)
        #    - Quebra de regra: A funcao faz duas coisas (ler arquivo e retornar dados completos ou uma linha)
        return _dados_globais.to_dict('records')

# 8. PEP 8: Espacamento
#    - Quebra de regra: Misturar espacos e tabs, e nao usar espacos ao redor de operadores
def main( _):

    # 9. PEP 8: Comprimento da Linha
    #    - Quebra de regra: Linha com mais de 79 caracteres
    nome_do_arquivo = "exemplo.csv" if len(sys.argv) < 2 else sys.argv[1]

    #
    # 10. SOLID - Principio da Inversao de Dependencia (DIP)
    #     - Quebra de regra: Modulo de alto nivel (main) depende diretamente de uma implementacao de baixo nivel (Processar_Dados_do_arquivo)
    #
    if nome_do_arquivo == "exemplo.csv" and not os.path.exists(nome_do_arquivo):
        # 11. Testes unitarios: nao existem
        #     - Quebra de regra: Nao ha testes para garantir que o codigo funciona
        print("Criando arquivo de exemplo...")
        pandas.DataFrame({"nome": ["João", "Maria", "Pedro"], "idade": [25, 30, 35], "cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]}).to_csv(nome_do_arquivo, index=False)

    dados = Processar_Dados_do_arquivo(nome_do_arquivo)
    print("Dados completos:\n", dados)

    uma_linha = Processar_Dados_do_arquivo(nome_do_arquivo, obter_uma_linha=True)
    print("\nUma linha aleatoria:\n", uma_linha)

if __name__ == '__main__':
    main(None)
