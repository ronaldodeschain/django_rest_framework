# API Escola - Django REST Framework

Este repositório contém o código-fonte de uma API RESTful para um sistema de escola, desenvolvida com Django e Django REST Framework. A API permite gerenciar o cadastro de estudantes e cursos.

## Funcionalidades

- **Gerenciamento de Estudantes**: CRUD (Criar, Ler, Atualizar, Deletar) para estudantes.
- **Gerenciamento de Cursos**: CRUD (Criar, Ler, Atualizar, Deletar) para cursos.

## Tecnologias Utilizadas

- **Python 3**
- **Django**
- **Django REST Framework**

## Pré-requisitos

Antes de começar, garanta que você tenha o seguinte instalado:
- Python 3.8+
- `pip` (gerenciador de pacotes do Python)
- `git` (para clonar o repositório)
- **Visual Studio Code** (editor de código recomendado)
- **Thunder Client**: Uma extensão do VS Code que funciona como um cliente REST leve.

### Por que usar o Thunder Client?

O **Thunder Client** é uma ferramenta essencial para testar e interagir com a API. Ele permite enviar requisições HTTP (GET, POST, PUT, DELETE, etc.) diretamente do editor de código, sem a necessidade de instalar programas externos como o Postman.

Com ele, você pode:
- Testar os endpoints da API para verificar se estão funcionando corretamente.
- Enviar dados (em formato JSON) para criar novos recursos (como um novo curso ou estudante).
- Depurar erros, analisando as respostas e os códigos de status retornados pela API.

## Instalação e Execução

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd django_rest_framework
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Linux / macOS
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    *(Obs: Recomenda-se criar um arquivo `requirements.txt` com `pip freeze > requirements.txt` para facilitar a instalação)*
    ```bash
    pip install django djangorestframework
    ```

4.  **Aplique as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

5.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

A API estará disponível em `http://127.0.0.1:8000/`.

## Endpoints da API

Use o Thunder Client para fazer requisições para os seguintes endpoints:

- `GET /estudantes/`: Lista todos os estudantes.
- `POST /estudantes/`: Cria um novo estudante.
- `GET /cursos/`: Lista todos os cursos.
- `POST /cursos/`: Cria um novo curso.

**Importante**: Ao usar o Django REST Framework com o `DefaultRouter`, lembre-se sempre de adicionar uma barra (`/`) ao final das URLs, como `/cursos/` e `/estudantes/`, para evitar erros de redirecionamento em requisições `POST`.
