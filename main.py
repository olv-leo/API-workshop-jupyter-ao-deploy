from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

produtos: List[Dict[str, any]] = [
    {
        "id": 1,
        "nome": "Produto 1",
        "descricao": "Descrição do Produto 1",
        "preco": 100.0,
    },
    {
        "id": 2,
        "nome": "Produto 2",
        "descricao": "Descrição do Produto 2",
        "preco": 200.0,
    },
    {
        "id": 3,
        "nome": "Produto 3",
        "descricao": "Descrição do Produto 3",
        "preco": 300.0,
    },
]


@app.get("/")
def ola_mundo():
    return {"Olá": "Pessoal!"}


@app.get("/produtos")
def listar_produtos():
    return produtos
