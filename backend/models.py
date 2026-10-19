from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field


class AvisoCreate(BaseModel):
  titulo: str = Field(..., min_length=4, max_length=60)
  autor: str = Field(..., min_length=3, max_length=50)
  prioridade: Literal["normal", "importante"]
  mensagem: str = Field(..., min_length=10, max_length=300)


class AvisoResponse(BaseModel):
  id: int
  titulo: str
  autor: str
  prioridade: Literal["normal", "importante"]
  mensagem: str
  publicado_em: str