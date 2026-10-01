# Lab 03 - Desafio M&A: Fusões, Aquisições e Inteligência Cross-Dataset

**Curso / Disciplina:** MBA em Business Intelligence and Analytics (BI) — Augmented Analytics & AI-Driven Insights (AA)  
**Ambiente:** Google AI Studio ([aistudio.google.com](https://aistudio.google.com/))  
**Linguagem / Stack:** Google Gemini Flash 3.8 (`gemini-3.8-flash`) / Cross-Dataset Reasoning / Strategic Analytics  
**Duração Estimada:** 25 a 30 minutos  

---

## 🎯 Objetivo do Lab

O objetivo deste laboratório é explorar a capacidade do modelo Gemini de realizar cruzamento semântico entre bases heterogêneas e não normalizadas (sem chaves primárias ou relacionamentos relacionais pré-existentes), simulando um comitê executivo de Fusões e Aquisições (M&A).

Ao final deste laboratório, você será capaz de:
1. Operar inferência simultânea sobre múltiplos arquivos tabulares em uma única janela de contexto.
2. Identificar gaps de demanda de clientes em uma base de CX e mapear soluções em um portfólio de empresas investíveis.
3. Conduzir análise de sinergia estratégica entre satisfação de consumidores e alocação de capital em P&D/Marketing.
4. Redigir uma tese de investimento executiva ("Investment Memorandum") fundamentada em evidências empíricas cruzadas.
5. Controlar o nível de ousadia e disrupção do comitê via ajuste de amostragem estocástica (**Top-P**).

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
3. Selecione o modelo: **Gemini Flash 3.8** (`gemini-3.8-flash`).
4. Configure os parâmetros técnicos:
   * **Temperature:** `0.4`
   * **Top-P:** `0.2` (início conservador focado em evidências numéricas)

### Passo 2: Configuração da Persona do Comitê de M&A
No campo **"System Instruction"**, insira a persona do consultor estratégico:

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

### Passo 5: Teste de Criatividade e Disrupção (Top-P)
1. Abra as configurações laterais (**Advanced Settings**).
2. Eleve o parâmetro **Top-P de 0.2 para 0.9** (mantendo temperature em 0.4 ou 0.6).
3. Submeta a seguinte provocação ao modelo:
   ```text
   Se decidirmos ignorar a sinergia imediata de curto prazo e priorizarmos disrupção tecnológica radical para dominar o mercado nos próximos 5 anos, sua recomendação de aquisição mudaria? Justifique.
   ```
4. Avalie como a ampliação do espaço probabilístico altera as prioridades da IA.

---

## 🧪 Validação & Critérios de Aceite

- [ ] Os dois arquivos foram ingeridos e reconhecidos na sessão ativa do AI Studio.
- [ ] A recomendação de M&A citou evidências e métricas concretas de ambos os arquivos.
- [ ] O modelo identificou com clareza a conexão de negócio entre o problema de CX e a solução da startup.
- [ ] A variação do Top-P demonstrou contraste claro entre conservadorismo financeiro e apetite por risco tecnológico.

---

## 💡 Desafios Complementares

* **Análise de Antissinergia (Due Diligence de Riscos):** Peça ao modelo: *"Quais são os 3 maiores riscos operacionais e culturais ao integrar a startup recomendada à nossa operação atual?"*.
* **Simulação de Negociação (Valuation):** Solicite uma estimativa de múltiplos de faturamento aceitáveis para a transação com base nas margens observadas.
