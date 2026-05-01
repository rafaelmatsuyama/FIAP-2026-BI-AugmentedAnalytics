# Lab 04: Chat with Data (Agente Analista Nativo)
**Disciplina:** Augmented Analytics & AI-Driven Insights
**Objetivo:** Explorar o dataset socioeconômico `adult.csv` usando um Agente de IA que gera código Pandas em tempo real.

---

### 1. Preparação do Ambiente
1. Abra o [Google Colab](https://colab.research.google.com/).
2. No menu lateral (ícone de pasta), faça o upload do arquivo: `Lab 04 - adult.csv`.
3. Importe o notebook fornecido pelo professor (`Lab 04 - Colab Notebook.ipynb`).       
4. Insira sua **API Key** do Google AI Studio na variável `API_KEY`.

### 2. O Desafio Analítico
Você agora tem um "Analista Digital" que traduz suas perguntas para código Python. Use a função `chat_com_dados("sua pergunta")` para responder a estas questões de negócio:

*   **Segmentação:** `chat_com_dados("Qual a principal ocupação das mulheres que ganham acima de 50k?")`
*   **Comportamento:** `chat_com_dados("Pessoas casadas trabalham mais horas por semana que solteiros?")`
*   **Educação:** `chat_com_dados("Quem tem mestrado (Masters) ganha proporcionalmente mais do que quem tem graduação (Bachelors)?")`
*   **Visualização:** `chat_com_dados("Gere um gráfico de pizza da distribuição de raça (RACE) na base.")`

### 3. Reflexão para o Board
*   Observe como a IA gera o código Python no "back-end" para responder sua pergunta.
*   Isso resolve o problema de falta de braço técnico no seu time?
*   Como validar se o código gerado pela IA está realmente correto?

---
*Dica: Você pode pedir gráficos complexos, como: chat_com_dados("Gere um gráfico de dispersão de Idade vs Horas por Semana colorindo por Sexo.")*
