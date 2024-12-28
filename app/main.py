from fastapi import FastAPI
from app.schema import ProdutosSchema
from app.data import Produtos
from typing import List

app = FastAPI()
lista_de_produtos = Produtos()


@app.get("/")
def ola_mundo():
    return {"Olá": "Mundo"}


@app.get("/produtos", response_model=List[ProdutosSchema])
def listar_produtos():
    return lista_de_produtos.listar_produtos()


@app.get("/produtos/{produto_id}", response_model=ProdutosSchema)
def buscar_produto(produto_id: int):
    return lista_de_produtos.buscar_produto(produto_id)


@app.post("/produtos", response_model=ProdutosSchema)
def add_produto(produto: ProdutosSchema):
    return lista_de_produtos.add_produto(produto.model_dump())
