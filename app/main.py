from app.schema import ProdutosSchema
from app.routes import router
from fastapi import FastAPI
from typing import List

app = FastAPI()

app.include_router(router)
