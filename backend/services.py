from datetime import datetime
from typing import List, Optional
from models import AvisoCreate, AvisoResponse

# Armazenamento em memória
avisos_db: List[dict] = []


def listar_avisos_service() -> List[dict]:
  return avisos_db


def criar_aviso_service(aviso_data: AvisoCreate) -> dict:
  novo_aviso = {
      "id": len(avisos_db) + 1,
      "titulo": aviso_data.titulo,
      "autor": aviso_data.autor,
      "prioridade": aviso_data.prioridade,
      "mensagem": aviso_data.mensagem,
      "publicado_em": datetime.now().strftime("%d/%m/%Y às %H:%M"),
  }
  avisos_db.append(novo_aviso)
  return novo_aviso


def deletar_aviso_service(aviso_id: int) -> bool:
  global avisos_db
  aviso_encontrado = False

  for aviso in avisos_db:
    if aviso["id"] == aviso_id:
      aviso_encontrado = True
      break

  if aviso_encontrado:
    avisos_db = [a for a in avisos_db if a["id"] != aviso_id]
    return True

  return False