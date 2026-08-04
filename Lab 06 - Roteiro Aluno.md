# Lab 06: Operação Flash Insight (Dify.ai)
**Disciplina:** Augmented Analytics & AI-Driven Insights
**Objetivo:** Orquestrar um fluxo multi-agente visual para análise de concorrência em tempo recorde.

---

### 🚨 CENÁRIO DE GUERRA
O CEO da sua empresa acaba de ver uma notícia sobre um novo produto lançado pelo maior concorrente. Ele precisa de um **Relatório de Impacto Estratégico** na mesa dele em 10 minutos. O time de BI está sobrecarregado. Sua missão é construir um fluxo automatizado no **Dify** que pesquise o concorrente e gere a análise de riscos.

### 🛠️ PREPARAÇÃO DO AMBIENTE
1. Acesse: [Dify.ai](https://dify.ai/) e faça login (Cloud).
2. Clique em **"Create from Blank"** -> **"Workflow"**.
3. Nomeie como: `Sinalizador_Concorrencia_MBA`.

### ⛓️ CONFIGURAÇÃO DO MODELO
1. Vá em Profile > Settings > Model Provider.
2. Selecione Gemini.
3. Adicione a sua API_KEY (use a que criamos no Google AI Studio).
4. Veja se a bolinha verde aparece próximo ao Config.

### ⛓️ CONSTRUÇÃO DO FLUXO (ORQUESTRAÇÃO)
Você deve conectar os seguintes "Nós" (Nodes):

1. **Start (Início):** Adicione um campo de entrada (User Input) do tipo Texto (Short Text) chamado `nome_concorrente`.
2. **LLM Node (Agente Pesquisador):**
   - **System Prompt:** "Você é um Especialista em Inteligência de Mercado. Sua tarefa é descrever o modelo de negócio e os pontos fortes do {nome_concorrente}."
   - Clique em + Add Message e no **User Prompt:** Analise o modelo de negócio da empresa {nome_concorrente}.
   - **Model:** `gemini-2.5-flash`.
3. **LLM Node (Agente de Estratégia):**
   - **Input:** Recebe o texto do Agente Pesquisador.
   - **System Prompt:** "Você é um Diretor de Estratégia. Com base na descrição do concorrente, identifique os 3 maiores riscos para a nossa empresa e sugira uma contraofensiva."
   - Clique em + Add Message e no **User Prompt:** Faça o Mapeamento de Riscos com  base nesse modelo de negócio: {Agente_Pesquisador.text}. Exiba  o relatório formatado em Markdown.
4. **End (Resultado Final):** Crie um Output com uma variável chamada `report` com o valor {Agente_Estrategia.text}.

### 🎯 A MISSÃO
- Execute o fluxo para o concorrente: **"OpenAI (lançamento do novo modelo)"**.
- O fluxo deve entregar o relatório final com: Resumo do Concorrente + Riscos + Contraofensiva.

### 🌪️ DICAS DE CAOS (TROUBLESHOOTING)
- **O nó não conecta:** Certifique-se de puxar a linha do ícone de "+" para o centro do próximo bloco.
- **Erro de Variável:** No segundo Agente, use a sintaxe `{{#node_id.text#}}` para referenciar a saída do primeiro.
- **Resposta Rasa:** Aumente a "Temperature" do Agente Pesquisador para 0.7 para captar mais nuances.

---
*Dica: No Dify, você pode adicionar um nó de 'Google Search' se tiver uma API Key, tornando o agente capaz de ler notícias de hoje.*
