from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

contatos = list()

class Contato(BaseModel):
    nome: str
    telefone: str
    email: str
    favorito: bool

@app.get("/")
def root():
    return contatos


@app.get("/contato/{pos}")
def get_contato(pos: int):
    return contatos[pos]

@app.post("/adicionar/")
def criar_contato(contato: Contato):
    contatos.append(contato)
    return len(contatos)

@app.put("/favoritar/{pos}")
def toggle_favorito(pos: int):
    if contatos[pos].favorito:
        contatos[pos].favorito = False
    else:
        contatos[pos].favorito = True
    return contatos[pos]

@app.delete("/deletar/{pos}")
def deletar_contato(pos: int):
    contato = contatos.pop(pos)
    return contato

@app.put("/editar/{pos}")
def editar_contato(pos: int, contato: Contato):
    contatos[pos] = contato
    return contatos[pos]
