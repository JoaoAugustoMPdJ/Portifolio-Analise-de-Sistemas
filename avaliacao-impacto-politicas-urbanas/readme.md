# Avaliação de Impacto de Políticas Públicas Urbanas com Machine Learning

Contexto urbano: Salvador – BA  
Domínios: Clima, Mobilidade Urbana e Segurança Pública  
Técnicas: Análise de Dados, Machine Learning e Avaliação Before/After  
Visualização: Dashboard interativo com Streamlit

## Descrição do Projeto

Este projeto propõe o desenvolvimento de um **framework genérico de análise urbana**, capaz de avaliar dados de diferentes domínios de políticas públicas por meio de técnicas de Análise de Dados e Machine Learning.

A solução foi pensada para que o **usuário possa escolher o domínio urbano e o tipo de análise**, sem a necessidade de alterar o código-fonte, tornando o sistema reutilizável, modular e escalável.

No momento o projeto utiliza dados simulados do contexto urbano brasileiro, com foco na cidade de Salvador (BA), e tem como finalidade apoiar análises exploratórias, previsões e avaliações de impacto de intervenções públicas.

##  Objetivos

- Desenvolver um pipeline genérico para análise de dados urbanos
- Permitir a análise de múltiplos domínios utilizando a mesma arquitetura
- Implementar visualizações automáticas orientadas por domínio
- Aplicar modelos de Machine Learning para previsão de séries temporais
- Avaliar impacto de intervenções públicas por meio de análises before/after
- Disponibilizar os resultados em um dashboard interativo

##  Domínios Urbanos Analisados

###  Clima
- Análise de séries temporais de variáveis climáticas
- Identificação de padrões sazonais
- Previsão de valores futuros com modelos de regressão

###  Mobilidade Urbana
- Análise de fluxo de veículos
- Identificação de horários críticos de congestionamento
- Previsão de tráfego urbano

###  Segurança Pública
- Análise de ocorrências criminais
- Identificação de períodos com maior incidência
- Avaliação de impacto de intervenções no tempo

##  Tipos de Análise Disponíveis

###  Análise Exploratória
- Visualização de séries temporais
- Estatísticas descritivas automáticas
- Identificação de tendências e padrões

###  Previsão com Machine Learning
- Modelos de Random Forest
- Previsões baseadas em dados históricos
- Comparação entre valores reais e previstos

###  Avaliação de Impacto (Before/After)
- Separação automática dos dados em períodos antes e depois
- Comparação de médias e variação percentual
- Visualização gráfica do impacto da intervenção


##  Arquitetura do Projeto

O projeto foi estruturado seguindo princípios de modularização e separação de responsabilidades.

avaliacao-impacto-politicas-urbanas/
│
├── app.py                     # Dashboard Streamlit
├── requirements.txt
├── README.md
│
├── data/
│   ├── clima/
│   ├── mobilidade/
│   └── seguranca/
│
├── src/
│   ├── pipeline.py            # Pipeline central genérico
│   │
│   ├── core/
│   │   ├── impact.py          # Avaliação before/after
│   │   └── visualization.py  # Visualizações
│   │
│   └── domains/
│       ├── clima.py
│       ├── mobilidade.py
│       └── seguranca.py
 ---

 ## Interface do Usuário

A aplicação conta com um dashboard interativo desenvolvido com Streamlit, permitindo ao usuário:

1. Selecionar o domínio urbano de interesse
2. Escolher o tipo de análise (exploração, previsão ou impacto)
3. Definir a data de intervenção, quando aplicável
4. Visualizar gráficos e métricas automaticamente geradas

##  Como Executar o Projeto

###  Instalar dependências
```bash
pip install -r requirements.txt

streamlit run app.py
```
## BLOCO 9 — Tecnologias Utilizadas

##  Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit

## Aplicação Acadêmica

Este projeto pode ser utilizado como:

- Trabalho acadêmico em cursos de Análise e Desenvolvimento de Sistemas
- Estudo de caso em Análise de Dados e Ciência de Dados
- Projeto de portfólio profissional
- Base para pesquisas sobre avaliação de políticas públicas urbanas

##  Possíveis Evoluções Futuras

- Integração com APIs de dados públicos
- Inclusão de mapas e análises geoespaciais
- Implementação de métodos causais (DiD, Causal Impact)
- Explicabilidade de modelos de Machine Learning
- Deploy da aplicação em ambiente web

##  Possíveis Evoluções Futuras

- Integração com APIs de dados públicos
- Inclusão de mapas e análises geoespaciais
- Implementação de métodos causais (DiD, Causal Impact)
- Explicabilidade de modelos de Machine Learning
- Deploy da aplicação em ambiente web

## Autor

João Augusto Moura Peixoto de Jesus
Recém-formado em Análise e Desenvolvimento de Sistemas  
Foco em Análise de Dados, Python, SQL e Visualização de Informações
