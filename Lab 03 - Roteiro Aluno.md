# Lab 03: Desafio M&A (Fusões e Aquisições)
**Disciplina:** Augmented Analytics & AI-Driven Insights
**Objetivo:** Cruzar inteligência de dois datasets distintos para fundamentar uma decisão de investimento estratégico.

---

### 1. Preparação do Ambiente
1. Acesse o [Google AI Studio](https://aistudio.google.com/).
2. No menu lateral, clique em **"Create New"** -> **"Chat Prompt"**.
3. Selecione o modelo: **Gemini 3 Flash Preview** (Este modelo possui um raciocínio superior para cruzamento de dados complexos).

### 2. Configurando o "Comitê de Investimentos"
No campo **"System Instruction"**, cole a seguinte persona:

> "Você é um Consultor Sênior de Fusões e Aquisições (M&A). Sua missão é analisar dois contextos distintos: o perfil dos meus clientes atuais e as startups disponíveis no mercado. Sua recomendação deve ser baseada em sinergia estratégica e ROI de longo prazo."

### 3. Upload de Múltiplos Arquivos
Desta vez, você fará o upload de **DOIS** arquivos simultaneamente (clique no ícone de `+` no campo de chat):
1. `Lab 01 - PesquisaClientes.csv` (Base de Clientes).
2. `Lab 02 - 50_Startups.csv` (Startups para Investimento).

### 4. O Desafio Estratégico
Execute o prompt abaixo para ver a IA cruzar as informações:

> "Baseado nos dados fornecidos:
> 1. Identifique nos dados de **Lab 01 - PesquisaClientes** qual o perfil demográfico (Idade/Salário) que apresenta a menor propensão de compra.
> 2. Agora, olhe para as startups no arquivo **Lab 02 - 50_Startups**. Qual dessas startups (ou categoria de gasto) possui a maior sinergia para resolver o problema desse grupo insatisfeito?
> 3. Crie um 'Executive Summary' justificando qual startup meu negócio deveria adquirir para expandir nossa participação de mercado, citando dados de ambos os arquivos."

### 5. Teste de Criatividade (Top-P)
Após a primeira resposta, vá em **Advanced Settings** e altere:
* **Top-P de 0.2 para 0.9.**
* Refaça a pergunta: *"Se fôssemos ignorar o lucro imediato e focar apenas em disrupção tecnológica, a recomendação mudaria?"*

---
*Dica: Observe como o Gemini 3 Flash Preview consegue criar conexões 'semânticas' entre os dois arquivos, mesmo que eles não tenham colunas em comum.*
