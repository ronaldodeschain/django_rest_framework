# API Escola - Django REST Framework

Este repositório contém o código-fonte de uma API RESTful para um sistema de escola, desenvolvida com Django e Django REST Framework. A API permite gerenciar o cadastro de estudantes, cursos e matrículas. **Este projeto foi concebido como um estudo prático focado na implementação de testes unitários e de integração em aplicações Django REST Framework.**

## Funcionalidades

- **Gerenciamento de Estudantes**: CRUD (Criar, Ler, Atualizar, Deletar) para estudantes.
- **Gerenciamento de Cursos**: CRUD (Criar, Ler, Atualizar, Deletar) para cursos.

-   **Gerenciamento de Matrículas**: Operações CRUD (Criar, Ler, Atualizar, Deletar) para matrículas.
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
    git clone https://github.com/ronaldodeschain/django_rest_framework.git
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
- `GET /matriculas/`: Lista todas as matrículas.
- `POST /matriculas/`: Cria uma nova matrícula.

**Importante**: Ao usar o Django REST Framework com o `DefaultRouter`, lembre-se sempre de adicionar uma barra (`/`) ao final das URLs, como `/cursos/` e `/estudantes/`, para evitar erros de redirecionamento em requisições `POST`.

## Testes

Este projeto inclui uma suíte de testes abrangente, demonstrando a aplicação de testes unitários e de integração para garantir a correção e a robustez da aplicação.

### Tipos de Testes

-   **Testes Unitários de Modelo**: Localizados em `escola/tests/test_models.py`, estes testes verificam o comportamento individual dos modelos (`Estudante`, `Curso`, `Matricula`), assegurando que a lógica de cada componente funcione como esperado.
-   **Testes de Integração de API**: Encontrados em `escola/tests/test_cursos.py`, `escola/tests/test_matriculas.py`, e `escola/tests/test_fixtures.py` (que valida o carregamento da fixture), estes testes utilizam `APITestCase` do Django REST Framework para simular requisições HTTP. Eles verificam o fluxo completo da API, incluindo listagem, criação, atualização e exclusão de recursos, e a interação com as fixtures.

### Executando os Testes

Para executar todos os testes do projeto, utilize o comando:

```bash
python manage.py test
```

Os testes dependem de uma fixture (`prototipo_banco.json`) que é carregada automaticamente no início da execução dos testes para popular o banco de dados de teste com dados iniciais consistentes.
