# Pads

Um projeto criado para aprender FastAPI, SQLAlchemy e comunicação assíncrona com JavaScript Vanilla. 
A aplicação permite acessar qualquer URL dinâmica e salvar textos automaticamente em um banco de dados SQLite.

## Tecnologias Utilizadas
- Python
- FastAPI
- SQLAlchemy (SQLite)
- HTML / CSS / JavaScript (com Debounce para Autosave)

## Como rodar localmente
1. Clone o repositório
2. Crie e ative um ambiente virtual (`python -m venv venv`)
3. Instale as dependências: `pip install -r requirements.txt`
4. Rode o servidor: `uvicorn main:app --reload`