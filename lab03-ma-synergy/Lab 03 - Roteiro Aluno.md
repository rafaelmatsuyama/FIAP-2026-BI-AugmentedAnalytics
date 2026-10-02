# Lab 03 - Desafio M&A: Fusões, Aquisições e Inteligência Cross-Dataset

**Curso / Disciplina:** MBA em Business Intelligence and Analytics (BI) — Augmented Analytics & AI-Driven Insights (AA)  
**Ambiente:** Google AI Studio ([aistudio.google.com](https://aistudio.google.com/))  
**Linguagem / Stack:** Google Gemini Flash (`gemini-3.8-flash`) / Cross-Dataset Reasoning / Strategic Analytics  
**Duração Estimada:** 25 a 30 minutos  

---

## 🎯 Objetivo do Lab

O objetivo deste laboratório é explorar a capacidade do modelo Gemini de realizar cruzamento semântico entre bases heterogêneas e não normalizadas (sem chaves primárias ou relacionamentos relacionais pré-existentes), simulando um comitê executivo de Fusões e Aquisições (M&A).

Ao final deste laboratório, você será capaz de:
1. Operar inferência simultânea sobre múltiplos arquivos tabulares em uma única janela de contexto multimodal.
2. Identificar gaps de demanda de clientes em uma base de CX e mapear soluções em um portfólio de empresas investíveis.
3. Conduzir análise de sinergia estratégica entre satisfação de consumidores e alocação de capital em P&D/Marketing.
4. Redigir uma tese de investimento executiva ("Investment Memorandum") fundamentada em evidências empíricas cruzadas.
5. Conduzir testes de estresse estratégico e dialética de comitê ("Advogado do Diabo") sob o paradigma de **Native Reasoning**.

---

## 📋 Pré-requisitos & Materiais

* Acesso ao [Google AI Studio](https://aistudio.google.com/).
* Datasets consumidos neste laboratório (disponíveis nos diretórios dos labs anteriores):
  * [`../lab01-cx-analytics/Lab 01 - PesquisaClientes.csv`](../lab01-cx-analytics/Lab%2001%20-%20PesquisaClientes.csv): Base de clientes e satisfação.
  * [`../lab02-financial-analytics/Lab 02 - 50_Startups.csv`](../lab02-financial-analytics/Lab%2002%20-%2050_Startups.csv): Base de startups e estrutura de custos.

---

## 🚀 Passo a Passo Guiado

### Passo 1: Preparação do Ambiente no AI Studio
1. Acesse [https://aistudio.google.com/](https://aistudio.google.com/).
2. No menu lateral, clique em **"Create New"** -> **"Chat Prompt"**.
3. Selecione o modelo: **Gemini 3.8 Flash** (`gemini-3.8-flash`).
4. Na barra lateral direita (**Run settings**), configure o motor de raciocínio:
   * **Thinking level:** Selecione **`High`**.
   * *Por que?* Cruzar bases de dados independentes sem chave estrangeira relacional exige raciocínio dedutivo em múltiplos saltos (*multi-hop reasoning*). O `Thinking: High` aloca orçamento de pensamento interno para o modelo testar hipóteses de complementaridade de mercado antes de formular a tese de investimento.

### Passo 2: Configuração da Persona do Comitê de M&A
No campo **"System instructions"** (painel direito), insira a diretriz de governança estratégica:

> *"Você é um Consultor Sênior de Fusões e Aquisições (M&A) e Corporate Venture Capital. Sua missão é cruzar dois contextos corporativos independentes: o perfil e as dores da base de clientes atuais e as capacidades operacionais das startups candidatas à aquisição. Sua recomendação deve demonstrar sinergia de produto, redução de churn e retorno financeiro sobre o capital empregado."*

### Passo 3: Ingestão Multi-Dataset
No chat prompt, utilize o ícone de upload (**`+`**) para anexar simultaneamente os dois arquivos:
1. `Lab 01 - PesquisaClientes.csv` (obtido da pasta `lab01-cx-analytics`)
2. `Lab 02 - 50_Startups.csv` (obtido da pasta `lab02-financial-analytics`)

### Passo 4: O Desafio Estratégico de Cruzamento
Submeta o prompt analítico estruturado:

```text
Com base nos dois datasets fornecidos, execute a seguinte análise de tese de aquisição:

1. Diagnóstico de Demanda (PesquisaClientes): Identifique qual segmento demográfico apresenta a menor propensão de compra e maior índice de atrito.
2. Mapeamento de Sinergia (50_Startups): Analise as startups disponíveis e aponte qual delas (ou perfil de gasto em Marketing vs. R&D) detém a melhor capacitação para solucionar o atrito desse público insatisfeito.
3. Tese Executiva de M&A: Apresente um 'Memorando de Investimento' justificando qual startup devemos adquirir, demonstrando a complementaridade entre as duas bases de dados.
```

### Passo 5: O Teste de Estresse da Tese (O "Advogado do Diabo")
Em comitês de M&A corporativo, teses de investimento consensuais costumam ocultar riscos graves de integração e execução. Sob o paradigma de *Native Reasoning*, testamos a solidez da recomendação provocando a IA a auditar criticamente suas próprias conclusões.

Submeta o prompt de provocação dialética:

```text
Agora atue como um membro cético e conservador do Comitê de Investimento ('Advogado do Diabo'):

1. Aponte os 3 principais riscos operacionais e culturais que poderiam fazer a aquisição recomendada no Memorando fracassar nos primeiros 12 meses.
2. Identifique se alguma outra startup do portfólio, com perfil mais focado em P&D (R&D) ou menor custo de aquisição, ofereceria uma relação risco-retorno superior no longo prazo.
```

*Saída Esperada:* O Gemini Flash utilizará sua cadeia interna de pensamento para dissecar vulnerabilidades da tese, avaliando trade-offs reais de integração, canibalização de base e alocação de risco.

---

## 🧪 Validação & Critérios de Aceite

Para validar a conclusão bem-sucedida do laboratório, certifique-se de que sua interação atendeu aos seguintes critérios:
- [ ] Os dois arquivos foram ingeridos e reconhecidos na sessão ativa do AI Studio sob o modelo `Gemini 3.8 Flash`.
- [ ] O comitê operou com `Thinking level: High`, evidenciando raciocínio dedutivo entre os dois datasets.
- [ ] A recomendação de M&A citou evidências e métricas concretas de ambos os arquivos (CX e Financeiro).
- [ ] O teste de estresse (Advogado do Diabo) gerou um debate executivo estruturado, apontando riscos de integração e alternativas de portfólio.

---

## 💡 Desafios Complementares

* **Validação Numérica com Code Execution:** Ative o toggle **Code execution** na barra de Tools do AI Studio e solicite: *"Calcule a margem de lucro exata e o percentual de gastos em Marketing sobre a receita de cada startup para embasar o valuation da aquisição."* Observe o modelo gerando código Python para calcular as métricas com precisão de máquina.
* **Simulação de Negociação & Estrutura de Pagamento (Earn-out):** Solicite uma proposta de estrutura de transação detalhando pagamento à vista (*upfront*) e parcelas condicionadas ao atingimento de metas de retenção de clientes (*earn-out*).
