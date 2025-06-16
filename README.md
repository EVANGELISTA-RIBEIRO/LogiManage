# LogiManage

## Descrição

O **LogiManage** é um sistema desenvolvido para gerenciar e otimizar a movimentação de equipamentos dentro de uma empresa. Ele oferece funcionalidades para controle de requisições de transporte, histórico de movimentações e geração de documentos, garantindo maior eficiência e organização nos processos logísticos.

## Funcionalidades

- **Gestão de Requisições de Transporte**:
  - Criação, edição e exclusão de requisições.
  - Geração automática de documentos de transporte.
  - Download de documentos em formatos adequados.

- **Histórico de Movimentações**:
  - Registro completo de todas as movimentações realizadas.

- **Testes Automatizados**:
  - Suporte a testes unitários e de integração utilizando `pytest` e `pytest-django`.

## Tecnologias Utilizadas

- **Linguagens de Programação**:
  - Python

- **Frameworks e Bibliotecas**:
  - Django
  - python-docx
  - pytest
  - pytest-django

- **Gerenciamento de Dependências**:
  - Poetry

## Requisitos do Projeto

- **Python**: Versão 3.10 ou superior.
- **Django**: Versão 5.1.7.
- **Banco de Dados**: Configuração compatível com o Django.

## Como Executar o Projeto

1. **Clone o repositório**:
  ```bash
   git clone <url-do-repositorio>
   cd LogiManage
   ```

2. **Execute o comando**:
  ```bash
   pjenv
   ```

3. **Instale as dependências:**
  ```bash
   poetry install
   ```

4. **Crie e aplique as migrações:**
  ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Execute o servidor de desenvolvimento:**
  ```bash
   python manage.py runserver
   ```