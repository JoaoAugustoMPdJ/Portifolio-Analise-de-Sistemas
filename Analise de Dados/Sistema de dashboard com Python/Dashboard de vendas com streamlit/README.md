# 📊 Dashboard de Vendas com Python

Este projeto apresenta um **dashboard interativo de vendas**, desenvolvido do zero em **Python**, utilizando **Streamlit, Pandas e Plotly**.  
O objetivo é demonstrar habilidades em **análise de dados, visualização interativa e construção de aplicações analíticas**, simulando um cenário real de negócio.

---

##  Objetivo do Projeto

- Criar um dashboard funcional sem dependência de banco de dados
- Trabalhar com dados estruturados em CSV
- Aplicar filtros dinâmicos
- Exibir indicadores de desempenho (KPIs)
- Construir visualizações interativas
- Seguir boas práticas de organização e clareza de código

---

##  Tecnologias Utilizadas

- **Python 3.13.2**
- **Streamlit** – Interface web interativa
- **Pandas** – Manipulação e análise de dados
- **Plotly Express** – Gráficos interativos
- **CSV** – Fonte de dados

---

##  Estrutura do Projeto

```text
Dashboard de vendas com streamlit
│
├── Dashboard.py          # Código principal do dashboard
├── vendas.csv      # Base de dados utilizada
└── README.md       # Documentação do projeto


## Funcionalidades

###  Visão Geral
- Faturamento total  
- Quantidade total de itens vendidos  
- Ticket médio  

### Filtro Dinâmico
- Filtro por produto com opção **"Todos"**
- Atualização automática dos indicadores, gráficos e tabela

###  Visualizações
- Gráfico de barras de faturamento por produto
- Gráfico de barras de quantidade vendida
- Tabela interativa com os dados filtrados

## Exemplo de Base de Dados (`vendas.csv`)

```csv
Produto,Quantidade,Valor Total
Notebook,10,15000
Mouse,40,5000
Teclado,25,7000
Monitor,15,12000
```

---

## ▶️ Como Executar o Projeto

### 1️⃣ Instalar as dependências
```bash
pip install streamlit pandas plotly
```

### 2️⃣ Executar o dashboard
```bash
streamlit run app.py
```

### 3️⃣ Acessar no navegador
```text
http://localhost:8501
```

---

## Conceitos Aplicados

- Análise exploratória de dados
- Criação de KPIs de negócio
- Filtragem dinâmica de dados
- Visualização de dados interativa
- Organização de código para aplicações analíticas

---

## Atualizações futuras

- Upload de arquivos CSV pelo usuário
- Integração com banco de dados SQL
- Publicação do dashboard online
- Autenticação de usuários
- Versão alternativa utilizando Dash

---

## Autor

**João Augusto Moura Peixoto de Jesus**  
Graduado em Análise e Desenvolvimento de Sistemas  
Foco em Análise de Dados, BI, Aplicações com Python e Banco de Dados (SQL)

---

 *Projeto desenvolvido para fins de aprendizado e portfólio profissional.*
