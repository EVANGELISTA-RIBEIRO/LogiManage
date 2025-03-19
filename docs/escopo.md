# Escopo - LogiManage

## 1. Introdução

### 1.1. Nome do projeto
**LogiManage** – Sistema de gerenciamento de movimentações de bens empresariais.

### 1.2. Breve descrição
O **LogiManage** é um sistema desenvolvido para facilitar e otimizar a gestão de movimentações de equipamentos dentro de uma empresa. Ele permite um controle do hitórico de movimentação de cada equipamento, garantindo um controle mais eficiente e seguro sobre os bens corporativos.

### 1.3. Objetivo principal
O principal objetivo do **LogiManage** é registrar o histórico completo das movimentações de cada equipamento, garantindo transparência no processo. Além disso, o sistema automatiza a geração de documentos essenciais para que as movimentações ocorram de forma rápida, organizada e padronizada, reduzindo a burocracia e minimizando erros operacionais.

## 2. Justificativa

### 2.1. Problema a ser resolvido
A gestão eficiente de movimentações de equipamentos dentro de uma empresa é essencial para garantir organização, segurança e otimização dos processos. No entanto, muitas empresas enfrentam desafios relacionados à falta de transparência e eficiência nesse controle.


O **LogiManage** surge como uma solução para enfrentar os seguintes problemas:

- **Falta de transparência**: Atualmente, a movimentação de equipamentos muitas vezes ocorre sem um sistema centralizado, dificultando a gestão e aumentando os riscos de perdas.
- **Ausência de histórico detalhado**: Sem um registro estruturado, é difícil identificar padrões, prevenir inconsistências e auditar movimentações anteriores, comprometendo a tomada de decisões estratégicas.
- **Desperdício de tempo em tarefas repetitivas**: Processos manuais, como preenchimento de formulários e geração de documentos, consomem um tempo significativo da equipe, reduzindo a produtividade.
- **Erros humanos no processo**: A falta de automação aumenta a probabilidade de falhas, como registros incorretos ou inconsistências nos documentos, o que pode levar a problemas operacionais e financeiros.

### 2.2. Benefícios esperados
A implementação do **LogiManage** trará diversos benefícios para a gestão de movimentações de equipamentos, otimizando processos e garantindo maior controle sobre os bens empresariais. Entre os principais ganhos, destacam-se:

- **Registro completo do histórico de movimentações**: Todas as transferências de equipamentos serão registradas no sistema, permitindo um acompanhamento detalhado e facilitando auditorias e consultas futuras.
- **Automação na geração de documentos**: O sistema criará automaticamente a **Requisição de Transporte**, garantindo que todas as movimentações sigam um processo padronizado, reduzindo o tempo gasto com burocracia.
- **Melhor aproveitamento do tempo da equipe**: Com a automação das tarefas repetitivas, os funcionários poderão direcionar seu tempo para atividades estratégicas e de maior valor para a empresa, aumentando a produtividade e eficiência operacional.

Além desses benefícios, o **LogiManage** contribuirá para a redução de erros manuais, a melhoria na transparência dos processos e a otimização da logística interna dos equipamentos.

### 2.3 Impacto do projeto
A implementação do **LogiManage** trará melhorias significativas na gestão de movimentação de bens empresariais, impactando diretamente a produtividade, a eficiência operacional e a transparência nos processos. Os principais impactos a longo prazo incluem:

- **Redução do tempo gasto com processos administrativos**: Com a automação da geração de documentos e registros de movimentação, estima-se uma diminuição significativa no tempo dedicado a tarefas burocráticas, permitindo que a equipe foque em atividades mais estratégicas.
- **Aumento da precisão nos registros**: A padronização e automação dos processos reduzirão erros humanos, garantindo informações mais confiáveis e auditáveis.
- **Melhoria na tomada de decisão baseada em dados**: Com um histórico estruturado de movimentações, os gestores terão acesso a insights valiosos para otimizar a alocação de equipamentos e reduzir desperdícios.
- **Escalabilidade e crescimento sustentável**: O LogiManage permitirá que a empresa lide com um volume maior de movimentações sem comprometer a eficiência, garantindo um modelo de gestão sustentável para o futuro.

## 3. Requisitos do Projeto

### 3.1. Requisitos funcionais
#### 1. Autenticação e Segurança
- Permitir login de usuários autenticados no sistema.
- Implementar funcionalidade de recuperação e troca de senha.
#### 2. Gestão de Requisições de Transporte
- Permitir que os usuários gerem uma Requisição de Transporte para movimentação de equipamentos.
- Possibilitar a edição de requisições de transporte antes da aprovação ou execução.
- Permitir a exclusão de requisições de transporte.
- Permitir o download do documento de Requisição de Transporte em formato adequado para documentação e arquivamento.

### 3.2. Requisitos não funcionais
#### 1. Escalabilidade
- O sistema deve ser capaz de suportar um número crescente de usuários e movimentações sem comprometer o desempenho.
- Deve permitir a adição de novas funcionalidades sem grandes impactos na arquitetura existente.
#### 2. Segurança
- Implementação de autenticação segura para acesso ao sistema.
- Armazenamento seguro de senhas.
- Proteção contra ataques comuns, como SQL Injection.
#### 3. Rapidez e Desempenho
- O sistema deve responder às requisições de usuários em um tempo mínimo, garantindo uma experiência fluida.
- Utilização de técnicas de otimização de banco de dados e cache para melhorar a performance.
- Interface leve e otimizada para carregamento rápido.

## 4. Tecnologias Utilizadas

### 4.1. Linguagens de programação
- Python
- JavaScript
- HTML
- CSS
### 4.2. Frameworks e bibliotecas
- Django
- PyMongo
- MongoEngine
- python-docx
- pdf2docx
- pytest
- ruff
### 4.3. Banco de dados
- MongoDBCompass
### 4.5. Ferramentas auxiliares
- Figma

## 5. Arquitetura do Sistema (A discutir)
- Diagrama de alto nível
- Definição de camadas (frontend, backend, banco de dados)

## 6. Metodologia de Desenvolvimento
### 6.1. Metodologia adotada
- Waterfall (Cascata)
- TDD (Test-Driven Development)
### 6.2. Ferramentas de gerenciamento
- GitLab

## 7. Cronograma (Necessário analisar o plano de ensino)
- Fases do projeto
- Marcos e entregas importantes
- Prazos estimados

## 8. Equipe e Responsabilidades

|Equipe          |Função                    |
|----------------|--------------------------|
|João Evangelista|Programador Back-End      |
|Rafael Arruda   |Programador Back-End      |
|Leandro Bezerra |UX/UI Designer            |
|Ademar          |Documentador              |
|Marcus          |Programador Front-End     |

## 11. Critérios de Aceitação
### 11.1. Cadastro do Transporte ao Banco de Dados
Objetivo: Garantir que uma requisição de transporte seja salva corretamente no banco de dados.
### 11.2. Edição de Transportes
Objetivo: Permitir que o usuário edite os dados de uma requisição de transporte existente.
### 11.3. Exclusão de Transportes
Objetivo: Permitir que o usuário exclua uma requisição de transporte.
### 11.4. Gerar Documento de Requisição de Transporte
Objetivo: Gerar e baixar um documento contendo os dados da requisição de transporte.
### 11.5. Cobertura de Testes de 100%
Objetivo: Garantir que todas as funcionalidades do sistema estejam cobertas por testes automatizados, atingindo 100% de cobertura.
