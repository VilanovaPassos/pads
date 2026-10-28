# Pads

Um bloco de notas minimalista e dinâmico na nuvem, inspirado no [Dontpad](https://dontpad.com/). Tudo o que você digita é salvo automaticamente e pode ser acessado de qualquer lugar por meio de URLs personalizadas.

O projeto foi desenvolvido com foco em performance e simplicidade, combinando o processamento assíncrono do **FastAPI** no backend com **JavaScript Vanilla** no frontend.

## Funcionalidades

- **Criação dinâmica de páginas:** acesse qualquer URL, como `/ideias`, e tenha uma página pronta para uso.
- **Autosave inteligente:** salvamento automático com *debounce* de 1 segundo, reduzindo requisições desnecessárias ao banco de dados.
- **Notificações visuais (Toast):** feedback discreto na tela a cada salvamento bem-sucedido.
- **Estrutura de subpáginas:** suporte a URLs aninhadas, como `/projetos/python`, com identificação automática de subpáginas e geração de um menu lateral de navegação (*sidebar*).
- **Página inicial dinâmica:** página explicativa que identifica automaticamente o domínio em que a aplicação está hospedada.
- **Prevenção de registros desnecessários:** rota específica para `/favicon.ico`, evitando que requisições automáticas dos navegadores gerem registros indevidos no banco de dados.
- **Docker Ready:** aplicação preparada para execução em containers Docker.

## Tecnologias utilizadas

| Categoria | Tecnologias |
|---|---|
| Backend | Python 3.12, FastAPI, Uvicorn |
| Banco de dados | SQLite, SQLAlchemy (ORM) |
| Frontend | HTML5, CSS3, Flexbox, JavaScript Vanilla |
| Templates | Jinja2 |
| Infraestrutura | Docker |

## Como executar localmente

### Pré-requisitos

- Python 3.12 ou superior
- Git

### 1. Clone o repositório

```bash
git clone https://github.com/VilanovaPassos/pads.git
cd pads
```

### 2. Crie e ative um ambiente virtual

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (Prompt de Comando):**

```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Inicie o servidor

```bash
uvicorn main:app --reload
```

### 5. Acesse a aplicação

Abra o navegador e acesse:

[http://localhost:8000](http://localhost:8000)

O parâmetro `--reload` habilita o recarregamento automático durante o desenvolvimento.

## Como executar com Docker

O Docker permite executar a aplicação em um ambiente isolado. Para preservar os dados, utilize um volume persistente para armazenar o banco SQLite.

### 1. Construa a imagem

Na raiz do projeto, execute:

```bash
docker build -t pads-app .
```

### 2. Crie um volume para persistência

```bash
docker volume create pads-db-volume
```

### 3. Inicie o container

```bash
docker run -d \
  --name pads-server \
  -p 8000:8000 \
  -v pads-db-volume:/app \
  pads-app
```

No Windows, você também pode executar o comando em uma única linha:

```powershell
docker run -d --name pads-server -p 8000:8000 -v pads-db-volume:/app pads-app
```

### 4. Acesse a aplicação

[http://localhost:8000](http://localhost:8000)

### Comandos úteis do Docker

Verificar os logs:

```bash
docker logs -f pads-server
```

Parar o container:

```bash
docker stop pads-server
```

Iniciar novamente:

```bash
docker start pads-server
```

Remover o container:

```bash
docker rm -f pads-server
```

> **Importante:** o volume `pads-db-volume` mantém os dados mesmo que o container seja removido. Não remova o volume se quiser preservar o banco de dados.

**Observação sobre persistência:** o caminho `/app` usado no volume deve corresponder ao diretório em que o banco SQLite é armazenado dentro do container. Se o banco estiver em outro diretório, ajuste o mapeamento conforme a configuração da aplicação.


## Objetivo do projeto

O Pads busca oferecer uma experiência simples e rápida para criar blocos de notas acessíveis por URL, sem a necessidade de criar uma conta ou configurar documentos manualmente.

O projeto também serve como oportunidade de aprendizado e aplicação prática de conceitos como APIs assíncronas, persistência de dados com ORM, desenvolvimento frontend e containerização com Docker.

## Autor

**Mateus Vilanova dos Passos**

- GitHub: [@VilanovaPassos](https://github.com/VilanovaPassos)

---

Desenvolvido com Python, FastAPI e JavaScript.
