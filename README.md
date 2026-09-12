# FitTrack DevOps

Projeto desenvolvido para a disciplina de DevOps com o objetivo de aplicar conceitos de versionamento, branches, testes automatizados e CI/CD.

## Tecnologias

- Python
- FastAPI
- Pydantic
- Pytest
- Git
- GitHub

## Funcionalidades

A API permite:

- Cadastrar exercícios
- Listar exercícios
- Atualizar exercícios
- Excluir exercícios

## Estrutura do projeto

```text
fittrack-devops/
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_main.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Instalação

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd fittrack-devops
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Executando a aplicação

Para iniciar a API:

```bash
uvicorn app.main:app --reload
```

A aplicação ficará disponível em:

```text
http://127.0.0.1:8000
```

A documentação automática do FastAPI estará disponível em:

```text
http://127.0.0.1:8000/docs
```

## Endpoints

### Página inicial

```http
GET /
```

Retorna uma mensagem indicando que a API está funcionando.

### Listar exercícios

```http
GET /exercises
```

Retorna todos os exercícios cadastrados.

### Cadastrar exercício

```http
POST /exercises
```

Exemplo de requisição:

```json
{
  "name": "Supino reto",
  "muscle_group": "Peito"
}
```

### Atualizar exercício

```http
PUT /exercises/{exercise_id}
```

Exemplo:

```json
{
  "name": "Supino inclinado",
  "muscle_group": "Peito"
}
```

### Excluir exercício

```http
DELETE /exercises/{exercise_id}
```

Remove um exercício utilizando seu ID.

## Testes automatizados

O projeto utiliza o Pytest para execução dos testes automatizados.

Para executar todos os testes:

```bash
python -m pytest -v
```

Atualmente são realizados testes para:

- Funcionamento da rota inicial
- Cadastro de exercícios
- Listagem de exercícios
- Atualização de exercícios
- Exclusão de exercícios
- Tentativa de exclusão de exercício inexistente

## Versionamento

O desenvolvimento do projeto utiliza Git e GitHub.

A branch principal é:

```text
main
```

O desenvolvimento das funcionalidades foi realizado inicialmente na branch:

```text
develop
```

As alterações são integradas à branch principal através de Pull Requests.

## CI/CD

Este projeto será utilizado durante a disciplina de DevOps para implementação de um fluxo de Integração Contínua e Entrega Contínua (CI/CD).

O fluxo será evoluído para incluir etapas como:

```text
Push / Pull Request
        ↓
GitHub Actions
        ↓
Instalação das dependências
        ↓
Execução dos testes
        ↓
Build
        ↓
Deploy
```

## Objetivo acadêmico

O objetivo deste projeto é aplicar na prática conceitos relacionados a:

- Controle de versão
- Git
- GitHub
- Branches
- Commits
- Pull Requests
- Testes automatizados
- Integração contínua
- Entrega contínua
- GitHub Actions

O projeto será evoluído ao longo da disciplina conforme novos conceitos de DevOps forem apresentados.