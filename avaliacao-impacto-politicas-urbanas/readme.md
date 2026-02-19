# Avaliação de Impacto de Políticas Públicas Urbanas com Machine Learning

**Contexto urbano:** Salvador – BA  
**Domínios analisados:** Clima, Mobilidade Urbana e Segurança Pública  
**Abordagem:** Análise de Dados, Machine Learning e Avaliação Before/After  
**Visualização:** Dashboard interativo com Streamlit  

---

##  Descrição do Projeto

Este projeto consiste no desenvolvimento de um **framework genérico para análise de dados urbanos**, capaz de processar, validar e analisar automaticamente diferentes tipos de dados relacionados a políticas públicas urbanas.

A solução foi projetada para ser **flexível e reutilizável**, permitindo que o usuário selecione o domínio de interesse (clima, mobilidade ou segurança) e o tipo de análise desejada diretamente pela interface, **sem necessidade de alterar o código-fonte**.

O sistema também é capaz de **identificar automaticamente o tipo de dado enviado**, evitando erros comuns como a seleção incorreta do domínio para um determinado conjunto de dados.

Atualmente, o projeto utiliza dados simulados inspirados no contexto urbano brasileiro, com foco na cidade de Salvador (BA), sendo ideal tanto para aplicações acadêmicas quanto para composição de portfólio profissional.

---

##  Objetivos

- Desenvolver um pipeline genérico para análise de dados urbanos
- Criar uma arquitetura modular e extensível por domínio
- Garantir robustez no tratamento de dados reais (incompletos ou desorganizados)
- Implementar visualizações automáticas orientadas ao domínio analisado
- Avaliar impacto temporal por meio de análises before/after
- Disponibilizar os resultados em um dashboard interativo

---

##  Domínios Urbanos Analisados

###  Clima
- Análise de séries temporais de variáveis climáticas
- Visualização de padrões e variações ao longo do tempo
- Preparação dos dados para análises futuras de previsão

###  Mobilidade Urbana
- Análise do fluxo médio de veículos
- Identificação de horários de maior congestionamento
- Consolidação temporal dos dados de tráfego

###  Segurança Pública
- Análise de ocorrências criminais ao longo do tempo
- Filtragem por tipo de crime e bairro
- Identificação de padrões temporais de incidência

---

##  Tipos de Análise Disponíveis

###  Análise Exploratória
- Visualização automática de séries temporais
- Estatísticas agregadas por período
- Identificação de tendências e padrões urbanos

###  Avaliação de Impacto (Before/After)
- Separação automática dos dados em períodos antes e depois
- Comparação de médias temporais
- Análise simples de variação após um ponto de corte

>  O ponto de intervenção é definido automaticamente como o meio da série temporal, garantindo funcionamento mesmo com dados limitados.

---

## Arquitetura do Projeto

O projeto foi estruturado com foco em **separação de responsabilidades**, facilitando manutenção e expansão futura.



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

##  Interface do Usuário

A aplicação conta com um dashboard interativo desenvolvido com **Streamlit**, permitindo ao usuário:

1. Selecionar o domínio urbano de interesse
2. Escolher o tipo de análise
3. Enviar arquivos CSV com dados reais ou simulados
4. Visualizar gráficos automaticamente gerados
5. Evitar erros de domínio por validação automática dos dados


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
- Scikit-learn
- Streamlit

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

