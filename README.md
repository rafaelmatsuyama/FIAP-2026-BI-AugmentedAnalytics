# Augmented Analytics & AI-Driven Insights — Interactive Lab Suite

[![FIAP MBA](https://img.shields.io/badge/FIAP-MBA%20Business%20Intelligence%20%26%20Analytics-ED145B?logo=fiap&logoColor=white)](https://www.fiap.com.br/)
![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Google Gemini](https://img.shields.io/badge/LLM-Gemini%20Flash%203.8-orange?logo=google)
![CrewAI](https://img.shields.io/badge/Orchestration-CrewAI%20%7C%20Dify-blueviolet)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green.svg)

> **Repositório oficial de laboratórios práticos e arquitetura de referência desenvolvido para o curso de [MBA em Business Intelligence and Analytics](https://www.fiap.com.br/) da FIAP.**  
> *Cobring: No-Code Analytics, White-Box AutoML, Sistemas Multi-Agentes (SMA), Orquestração Visual (Dify), Squads de IA (CrewAI) e Agentic Dashboards (Streamlit).*

---

## 🎯 Visão Executiva & O Grande Salto Cognitivo

O paradigma analítico corporativo passou por uma mutação estrutural: os **Dashboards reativos tradicionais** exigem que tomadores de decisão naveguem por dezenas de filtros estáticos em busca de anomalias passadas. 

Esta disciplina inaugura o **Agentic Analytics**: uma abordagem onde modelos de linguagem de última geração (**Google Gemini Flash 3.8**) e squads de agentes autônomos assumem a esteira diagnóstica e prescritiva, gerando código Python transparente ("White-Box AutoML") e relatórios executivos em tempo real.

---

## 🧭 Catálogo Geral de Laboratórios

| Lab | Tópico Central | Stack & Plataforma | Entregável / Acesso Rápido |
| :---: | :--- | :--- | :---: |
| **01** | **O Analista de CX No-Code** | Google AI Studio • `gemini-3.8-flash` | [`lab01-cx-analytics/`](./lab01-cx-analytics/) |
| **02** | **O Analista Programável (VC)** | Python • Pandas • Gemini SDK | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rafaelmatsuyama/FIAP-2026-BI-AugmentedAnalytics/blob/main/lab02-financial-analytics/Lab%2002%20-%20Colab%20Notebook.ipynb) |
| **03** | **Desafio M&A (Cross-Dataset)** | Google AI Studio • Top-P Tuning | [`lab03-ma-synergy/`](./lab03-ma-synergy/) |
| **04** | **Agente Analista Nativo (Pandas)** | Python • Google Colab • Pandas Agent | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rafaelmatsuyama/FIAP-2026-BI-AugmentedAnalytics/blob/main/lab04-pandas-agent/Lab%2004%20-%20Colab%20Notebook.ipynb) |
| **05** | **AutoML Nativo (Scikit-Learn)** | Python • Random Forest • Churn | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rafaelmatsuyama/FIAP-2026-BI-AugmentedAnalytics/blob/main/lab05-automl-scikit/Lab%2005%20-%20Colab%20Notebook.ipynb) |
| **06** | **Orquestração Visual com Dify** | Dify.ai • Fluxos Visuais de LLM | [`lab06-dify-workflow/`](./lab06-dify-workflow/) |
| **07** | **Operação Churn Zero (Squads)** | CrewAI • LiteLLM • Multi-Agent | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rafaelmatsuyama/FIAP-2026-BI-AugmentedAnalytics/blob/main/lab07-crewai-squad/Lab%2007%20-%20Colab%20Notebook.ipynb) |
| **08** | **Refinamento e JSON Schema** | Google AI Studio • Saídas Estruturadas | [`lab08-json-schema/`](./lab08-json-schema/) |
| **09** | **Dashboard de Analytics Agentic** | Streamlit • PyNgrok • Colab | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rafaelmatsuyama/FIAP-2026-BI-AugmentedAnalytics/blob/main/lab09-agentic-dashboard/Lab%2009%20-%20Dashboard%20de%20Analytics.ipynb) |
| **10** | **A Grande Integração Final** | Streamlit • JSON Schema • Full Stack | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rafaelmatsuyama/FIAP-2026-BI-AugmentedAnalytics/blob/main/lab10-integracao-final/Lab%2010%20-%20Integração%20Final%20e%20Dashboard%20Estruturado.ipynb) |

---

## 🚀 Como Executar os Laboratórios

### Opção 1: Execução Direta no Google Colab (Recomendada)
Para os laboratórios baseados em Jupyter Notebooks (Labs 02, 04, 05, 07, 09 e 10):
1. Clique no botão **"Open In Colab"** correspondente na tabela acima.
2. O notebook será aberto diretamente na sua conta do Google Colab sem necessidade de clone local.
3. Carregue o dataset correspondente indicado no roteiro do laboratório na aba lateral de arquivos do Colab.

### Opção 2: Clone do Repositório
Caso deseje clonar e inspecionar todos os roteiros e datasets localmente:
```bash
git clone https://github.com/rafaelmatsuyama/FIAP-2026-BI-AugmentedAnalytics.git
cd FIAP-2026-BI-AugmentedAnalytics
```

### Opção 3: Google AI Studio
Para os laboratórios conceituais e semânticos (Labs 01, 03 e 08):
1. Acesse [https://aistudio.google.com/](https://aistudio.google.com/).
2. Siga as orientações descritas no respectivo `Roteiro Aluno.md` de cada pasta.

---

## 🛡️ Governança & Credenciais de API
- Os laboratórios utilizam o motor **Gemini Flash 3.8** (`gemini-3.8-flash`) com suporte a cotas gratuitas (**Free Tier**).
- Obtenha sua credencial em: [Google AI Studio - Get API Key](https://aistudio.google.com/).
- **Atenção à Segurança:** Nunca comite ou compartilhe publicamente seus notebooks com a variável `API_KEY` preenchida com sua chave real.
