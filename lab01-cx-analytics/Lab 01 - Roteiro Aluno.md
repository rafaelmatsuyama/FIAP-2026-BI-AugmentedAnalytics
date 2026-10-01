# Lab 01 - O Analista de CX No-Code com Google AI Studio e Gemini Flash 3.8

**Curso / Disciplina:** MBA em Business Intelligence and Analytics (BI) — Augmented Analytics & AI-Driven Insights (AA)  
**Ambiente:** Google AI Studio ([aistudio.google.com](https://aistudio.google.com/))  
**Linguagem / Stack:** Google Gemini Flash 3.8 (`gemini-3.8-flash`) / Prompt Engineering / No-Code Analytics  
**Duração Estimada:** 25 a 30 minutos  

---

## 🎯 Objetivo do Lab

O objetivo deste laboratório é transformar dados brutos e pesquisas de satisfação de clientes (CX) em inteligência diagnóstica e recomendações prescritivas acionáveis para o C-Level, utilizando o estado da arte em Large Language Models (LLMs) nativos sem dependência de código ou infraestrutura local.

Ao final deste laboratório, você será capaz de:
1. Configurar Personas Executivas no Google AI Studio por meio de **System Instructions** especializadas.
2. Calibrar hiperparâmetros de inferência analítica (**Temperature 0.5** e **Top-P 0.2**) para mitigar alucinações e assegurar ancoragem estatística.
3. Ingerir e analisar bases tabulares (`Lab 01 - PesquisaClientes.csv`) explorando a ampla janela de contexto do modelo.
4. Executar uma esteira analítica em 3 níveis: **Descritiva** (KPIs de CX), **Diagnóstica** (Segmentação Crítica de Insatisfação) e **Prescritiva** (Alocação de R$ 100k para contenção de Churn).
5. Contrastar a agilidade do **Agentic Analytics** frente às limitações de ferramentas legadas de BI e ETL No-Code.

---

## 📋 Pré-requisitos & Materiais

* Navegador Web moderno (Chrome, Edge ou Firefox).
* Conta Google ativa para autenticação no [Google AI Studio](https://aistudio.google.com/).
* Dataset fornecido neste laboratório:
  * [`Lab 01 - PesquisaClientes.csv`](./Lab%2001%20-%20PesquisaClientes.csv): Base de respostas de pesquisa de clientes com variáveis demográficas, pontuações de satisfação e comentários abertos.

---

## 🚀 Passo a Passo Guiado

### Passo 1: Acesso ao Google AI Studio & Seleção de Modelo
1. Acesse o portal oficial: [https://aistudio.google.com/](https://aistudio.google.com/).
2. Faça login com sua conta Google institucional ou pessoal.
3. No painel superior direito (seletor de modelo), selecione:
   * **Modelo:** `Gemini Flash 3.8` (ou string correspondente: `gemini-3.8-flash`).

### Passo 2: Calibração de Hiperparâmetros Analíticos
Na barra lateral direita (**Advanced Settings** ou painel de configuração), ajuste os controles de amostragem para análise determinística:
* **Temperature:** `0.5` *(Previne divagações poéticas e mantém a coerência factual sem tornar a resposta excessivamente rígida)*.
* **Top-P:** `0.2` *(Filtra o núcleo probabilístico da distribuição, priorizando os termos com maior probabilidade matemática de acerto analítico)*.

### Passo 3: Injeção da Persona Executiva (System Instruction)
Localize o campo **"System Instruction"** (no painel direito da interface) e cole a seguinte diretriz de governança:

> *"Você é um Diretor de Customer Experience (CX) e Estratégia Corporativa com 20 anos de experiência em retenção de clientes e análise de valor de vida (LTV). Sua missão é analisar dados quantitativos e qualitativos de satisfação, identificar correlações não óbvias entre variáveis demográficas e notas de atendimento, e propor planos de ação com foco estrito em contenção de churn e geração de ROI."*

### Passo 4: Carga de Dados na Janela de Contexto
1. No campo de mensagem (chat prompt), clique no botão **`+`** (Upload / Add file).
2. Selecione o arquivo [`Lab 01 - PesquisaClientes.csv`](./Lab%2001%20-%20PesquisaClientes.csv).
3. Observe que o arquivo é anexado diretamente ao prompt, utilizando a janela de contexto multimodal do Gemini para leitura integral da base sem necessidade de pré-processamento SQL.

### Passo 5: Execução da Esteira Analítica Multi-Estágio
Envie os prompts abaixo em sequência para explorar a capacidade analítica da IA:

#### Prompt 1 — Análise Descritiva (KPIs Críticos):
```text
Com base nos dados carregados, forneça um sumário executivo em formato de tabela contendo os principais indicadores de Customer Experience (NPS geral estimado, nota média por faixa etária e índice de insatisfação).
```
*Saída Esperada:* Tabela estruturada consolidando médias e volume de clientes por estrato demográfico.

#### Prompt 2 — Análise Diagnóstica (Correlações Críticas):
```text
Qual segmento demográfico (cruzando Idade, Ocupação e Estado Civil) apresenta a taxa mais crítica de insatisfação? Explique os fatores qualitativos nos comentários que justificam essa nota baixa.
```
*Saída Esperada:* Identificação de padrões não óbvios (ex: profissionais sobrecarregados ou faixas específicas com fricção no atendimento).

#### Prompt 3 — Análise Prescritiva (Alocação de Capital):
```text
Assuma que temos um orçamento emergencial de R$ 100.000 para estancar a perda de receita decorrente da insatisfação desse grupo crítico. Crie um plano de ação tático em 3 passos estruturados (Ação, Prazo de Execução e KPI de Sucesso) para recuperar esse segmento no próximo trimestre.
```
*Saída Esperada:* Proposta executiva viável orientada a ROI, indicando onde alocar o capital para máximo impacto.

---

## 🧪 Validação & Critérios de Aceite

Para validar a conclusão bem-sucedida do laboratório, certifique-se de que sua interação com o modelo atendeu aos seguintes requisitos:
- [ ] O modelo selecionado e ativo é o `Gemini Flash 3.8` com Temperature `0.5` e Top-P `0.2`.
- [ ] O arquivo `Lab 01 - PesquisaClientes.csv` foi interpretado sem truncamento ou falha de parsing.
- [ ] O diagnóstico identificou com clareza o segmento com maior concentração de insatisfação.
- [ ] As recomendações prescritivas foram orçadas dentro do limite estabelecido (R$ 100k) com métricas de mensuração claras.

---

## 💡 Desafios Complementares (Para Alunos Avançados)

* **Teste de Sensibilidade Estocástica:** Altere a **Temperature para 1.0** e o **Top-P para 0.9**. Execute novamente o Prompt 3 e compare o plano gerado: ele se tornou mais visionário ou perdeu o rigor estatístico?
* **Análise de Fricção Textual:** Peça ao modelo: *"Faça uma análise de sentimento específica sobre a menção a tempos de espera e relacione isso com o churn projetado em 6 meses."*
