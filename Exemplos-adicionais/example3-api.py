# -*- coding: utf-8 -*-
#
# Este arquivo ignora boas praticas de API, validacao e arquitetura de software.
#
# Para rodar este codigo:
# 1. Instale FastAPI: pip install fastapi
# 2. Instale Uvicorn: pip install uvicorn
# 3. Instale Pandas: pip install pandas
# 4. Salve um arquivo chamado 'dados.csv' no mesmo diretorio com colunas 'id', 'nome', 'idade' e 'cidade'.
# 5. Rode o arquivo: uvicorn api_fastapi_bad_practices:app --reload
#
# A seguir, um guia de endpoints:
# GET /
# POST /
# GET /<id_parametro>
# PUT /<id_parametro>
# DELETE /<id_parametro>
#
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import os
import random
import sys

# 1. SOLID - Principio da Responsabilidade Unica (SRP)
#    - Quebra de regra: A classe 'Item' serve tanto para a validacao do Pydantic quanto para um modelo de dados nao relacionado.
class Item(BaseModel):
    id: int
    nome: str
    idade: int
    cidade: str
    
    # 2. Reuso de codigo e classes mal definidas
    #    - Quebra de regra: A mesma classe e' usada para criar e atualizar, mesmo que alguns campos pudessem ser opcionais.
    #    - Quebra de regra: Sem validacao extra.
    

app = FastAPI()

# 3. Variaveis globais e estado mutavel
#    - Quebra de regra: O DataFrame e' uma variavel global que e' acessada e modificada em multiplas funcoes sem controle
#      e sem seguranca de thread.
if not os.path.exists("dados.csv"):
    # 4. Nao usar o 'with' para gerenciar arquivos
    #    - Quebra de regra: Abrir e fechar arquivos manualmente
    f = open("dados.csv", 'w')
    f.write("id,nome,idade,cidade\n")
    f.write(f"1,joao,{random.randint(18, 60)},Sao Paulo\n")
    f.close()

# 5. Tratamento de Erros: "engolir" excecoes genericas
#    - Quebra de regra: Usar um try-except que ignora qualquer erro na carga inicial
try:
    dados_globais = pd.read_csv("dados.csv")
except Exception:
    dados_globais = pd.DataFrame(columns=['id', 'nome', 'idade', 'cidade'])

# 6. Sem modularizacao
#    - Quebra de regra: Todas as funcoes de manipulacao de dados e a logica da API estao no mesmo arquivo, sem separacao de responsabilidades
#      (controllers, services, repositories).

@app.get("/")
def read_all_itens():
    return dados_globais.to_dict('records')

@app.post("/")
def create_item(item: Item):
    # 7. Seguranca: Nao validar entrada de usuario e nao ter autenticacao
    #    - Quebra de regra: Aceita qualquer JSON e nao requer autenticacao.
    # 8. Logs e Debug: Nao usar o modulo logging
    #    - Quebra de regra: Usar `print` em vez de um logger com niveis de severidade
    print("Item para criar:", item)
    global dados_globais
    novo_id = dados_globais['id'].max() + 1 if not dados_globais.empty else 1
    # 9. SOLID - Principio da Substituicao de Liskov (LSP)
    #    - Quebra de regra: Usar ._append() que e' um metodo interno e pode mudar.
    dados_globais = dados_globais._append(item.dict(), ignore_index=True)
    dados_globais.loc[dados_globais.id.isnull(), 'id'] = novo_id
    dados_globais.to_csv("dados.csv", index=False)
    return {"status": "adicionado", "dados": item.dict()}

@app.get("/{id_parametro}")
def read_item(id_parametro: int):
    # 10. Eficiencia de Codigo: Iterar sobre a lista inteira para encontrar um item
    #     - Quebra de regra: Nao usar o metodo otimizado de busca do Pandas
    for index, row in dados_globais.iterrows():
        if row['id'] == id_parametro:
            return row.to_dict()
    raise HTTPException(status_code=404, detail="Item nao encontrado")

@app.put("/{id_parametro}")
def update_item(id_parametro: int, item_atualizado: Item):
    global dados_globais
    # 11. Quebra de regra: Nao validar se o ID existe de forma eficiente
    idx = dados_globais.index[dados_globais['id'] == id_parametro].tolist()
    if not idx:
        raise HTTPException(status_code=404, detail="Item nao encontrado")
    
    dados_globais.loc[idx[0], :] = item_atualizado.dict()
    dados_globais.to_csv("dados.csv", index=False)
    return {"status": "atualizado", "dados": item_atualizado.dict()}

@app.delete("/{id_parametro}")
def delete_item(id_parametro: int):
    global dados_globais
    # 12. Quebra de regra: Nao ter confirmacao para a delecao
    dados_globais = dados_globais[dados_globais['id'] != id_parametro]
    dados_globais.to_csv("dados.csv", index=False)
    return {"status": "deletado"}
