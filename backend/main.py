from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from models import AvisoCreate, AvisoResponse
from services import (
    criar_aviso_service,
    deletar_aviso_service,
    listar_avisos_service,
)

app = FastAPI(title="Mural de Avisos Acadêmicos API")

# Configuração do CORS para o front-end na porta 5500
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(
    "/api/avisos", response_model=list[AvisoResponse], status_code=status.HTTP_200_OK
)
def listar_avisos():
    return listar_avisos_service()


@app.post(
    "/api/avisos", response_model=AvisoResponse, status_code=status.HTTP_201_CREATED
)
def publicar_aviso(aviso: AvisoCreate):
    return criar_aviso_service(aviso)


@app.delete("/api/avisos/{aviso_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_aviso(aviso_id: int):
    sucesso = deletar_aviso_service(aviso_id)
    if not sucesso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Aviso com ID {aviso_id} não encontrado.",
        )
    return None