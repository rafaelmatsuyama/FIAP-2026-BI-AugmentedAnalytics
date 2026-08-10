# Lab 10: A Grande Integração - Dashboard Agentic Estruturado (UI + JSON)

## 🏢 1. Contexto Executivo (Business Case)
Nas etapas anteriores, você desenvolveu os dois pilares fundamentais da inteligência artificial aplicada aos negócios:
1. **O Cérebro (Lab 08):** Uma IA com tom executivo e contrato rígido de dados via **JSON Schema**.
2. **A Carcaça (Lab 09):** Um dashboard interativo e dinâmico construído 100% em Python com **Streamlit**.

Sua missão neste laboratório é realizar a **"Cirurgia Técnica Final"**: conectar o cérebro refinado à interface web, criando um produto analítico completo de **Insight-as-a-Service**. O dashboard receberá dados brutos, acionará a Squad de IAs e renderizará cards executivos com métricas e recomendações acionáveis para a diretoria.

---

## 🎯 2. Entregáveis Técnicos
Ao concluir este laboratório, você terá entregue:
1. **Frontend Inteligente:** Dashboard em Streamlit consumindo dados estruturados em tempo real.
2. **Pipeline Resiliente:** Extração segura de JSON via regex (`re.search`) e persistência de sessão (`st.session_state`).
3. **Visão Board-Ready:** Componentes visuais com métricas de impacto (`st.metric`), alertas estratégicos e bloco de auditoria de dados (`st.json`).

---

## 🚀 3. Passo a Passo: Acesso e Configuração

### A. Google Colab (Seu Workbench)
1. **Acesse:** [colab.new](https://colab.new) e faça o upload do notebook `Lab 10 - Integração Final e Dashboard Estruturado.ipynb`.
2. **Execução Sequencial:** Execute a Célula 1 (Instalação das dependências `crewai`, `streamlit`, `pyngrok`).

### B. Ngrok Token (Túnel de Acesso)
1. **Acesse:** [ngrok.com](https://ngrok.com) e copie o seu **Authtoken**.
2. **Configuração:** Cole o token na variável `NGROK_TOKEN` na Célula 3 para habilitar a URL pública de acesso.

---

## 🛠️ 4. Fluxo de Execução do Lab

1. **Geração do App Integrado (`app.py`):** Execute a Célula 2 do notebook para compilar a lógica da aplicação.
2. **Ativação do Túnel:** Execute a Célula 3 e clique no link público gerado (`https://...ngrok-free.app`).
3. **Autenticação:** Insira sua **Gemini API Key** no painel lateral (Sidebar).
4. **Carga do Dataset:** Faça o upload do arquivo `PesquisaClientes.csv` (ou outro dataset de teste).
5. **Disparo da Squad:** Clique em **"🚀 Gerar Análise Estruturada"** e acompanhe o processamento da Squad.
6. **Auditoria dos Resultados:**
   - Verifique os cards de **Título do Insight** e **Métrica Crítica**.
   - Analise a tag de **Impacto Estimado** (Baixo, Médio ou Alto) e a **Recomendação Estratégica**.
   - Expanda a seção **Raw JSON** para auditar a integridade técnica da resposta.

---

## ⚠️ 5. Troubleshooting & Dicas de Sobrevivência
- **JSON Não Carrega na Tela:** Se houver erro de formatação, certifique-se de que o modelo utilizado é o `"google/gemini-3-flash-preview"`.
- **Sessão Reinicia no Clique:** O notebook utiliza `st.session_state` para reter as métricas na tela; evite recarregar a página do navegador (F5) durante o teste.
- **Timeout na Análise:** O script envia uma amostra controlada (`df.head(15)`) para garantir respostas ultra-rápidas sem estourar o limite de tokens da API.

---
*Material desenvolvido para o MBA em BI & Analytics - FIAP.*
