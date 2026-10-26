from sqlalchemy import Column, Integer, String, Text
from database import Base

class Pagina(Base):
    __tablename__ = "paginas"

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String, unique=True)

    conteudo = Column(Text, default="")