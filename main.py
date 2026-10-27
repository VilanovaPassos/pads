from fastapi import FastAPI, Depends, HTTPException, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import models, schemas
from database import engine, SessionLocal

#cria o arquivo e a tabela 
models.Base.metadata.create_all(bind=engine)

#Aponta para a pasta onde estão os templates HTML
templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

#função para criar a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



#========================= Rotas API ========================

@app.get("/api/{nome_pagina}")
def ler_pagina(nome_pagina: str, db: Session = Depends(get_db)):
    #Tenta achar a página no banco de dados
    pagina = db.query(models.Pagina).filter(models.Pagina.nome == nome_pagina).first()


    if not pagina:
        pagina = models.Pagina(nome=nome_pagina, conteudo="")
        db.add(pagina)
        db.commit()
        db.refresh(pagina)

    return {"nome": pagina.nome, "conteudo": pagina.conteudo}


@app.put("/api/{nome_pagina}")
def atualizar_pagina(nome_pagina: str, pagina_update: schemas.PaginaUpdate, db: Session = Depends(get_db)):
    pagina = db.query(models.Pagina).filter(models.Pagina.nome == nome_pagina).first()

    if not pagina:
        raise HTTPException(status_code=404, detail="Página não encontrada")

    #atualiza o conteúdo da página
    pagina.conteudo = pagina_update.conteudo
    db.commit()
    db.refresh(pagina)

    return {"nome": pagina.nome, "conteudo": pagina.conteudo}

#========================= Rotas PAGINAS ========================

@app.get("/")
def pagina_inicial(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html"
    )

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)

@app.get("/{nome_pagina}")
def renderiza_pagina(request: Request, nome_pagina: str):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"nome_pagina": nome_pagina}
    )