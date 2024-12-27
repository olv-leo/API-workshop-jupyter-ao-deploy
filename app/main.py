from fastapi import FastAPI
from app.schema import ProdutosSchema
from app.data import Produtos

app = FastAPI()
produtos = Produtos()


@app.get("/")
def ola_mundo():
    return {"Olá": "Mundo"}


@app.get("/produtos", response_model=list[ProdutosSchema])
def listar_produtos():
    return produtos.listar_produtos()


@app.get("/produtos/{produto_id}", response_model=ProdutosSchema)
def buscar_produto(produto_id: int):
    return produtos.buscar_produto(produto_id)
