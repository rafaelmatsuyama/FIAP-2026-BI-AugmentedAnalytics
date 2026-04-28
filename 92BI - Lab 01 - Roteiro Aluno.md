# Lab 01: O Analista de CX No-Code
**Disciplina:** Augmented Analytics & AI-Driven Insights
**Objetivo:** Transformar dados brutos de pesquisa em recomendações estratégicas usando o Gemini 3.

---

### 1. Preparação do Ambiente
1. Acesse o [Google AI Studio](https://aistudio.google.com/).
2. Faça login com sua conta Google.
3. No topo direito, selecione o modelo: **Gemini 3 Flash Preview**.

### 2. Configurando o Agente (System Instruction)
No campo **"System Instruction"** (localizado à direita na tela, conforme o novo layout), cole o seguinte comando:

> "Você é um Diretor de CX. Analise o CSV de satisfação e encontre correlações não óbvias entre demografia e insatisfação que geram perda de receita."

### 3. Ajustando os Parâmetros
Na barra lateral (em **Advanced Settings**), configure:
* **Temperature:** 0.5
* **Top-P:** 0.2

### 4. Upload dos Dados
No campo de chat, clique no ícone de **"+"** e faça o upload do arquivo: `PesquisaClientes.csv`.

### 5. O Desafio Prático
Execute os prompts abaixo para extrair os insights:

1. **Nível 1 (Descritivo):** "Peça um sumário executivo com os KPIs críticos identificados nos dados."
2. **Nível 2 (Diagnóstico):** "Qual segmento demográfico é mais crítico e por quê?"
3. **Nível 3 (Prescritivo):** "Crie um plano de ação de 3 passos para reverter a nota desse grupo específico."

---
*Dica: Observe como a precisão do modelo Gemini 3 permite identificar nuances nas respostas qualitativas.*
