from typing import List, Dict


class Produtos:
    def __init__(self):
        self.produtos = [
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

    def listar_produtos(self):
        return self.produtos

    def buscar_produto(self, produto_id):
        for produto in self.produtos:
            if produto["id"] == produto_id:
                return produto
        return {"mensagem": "Produto não encontrado"}

    def add_produto(self, produto):
        self.produtos.append(produto)
        return produto
