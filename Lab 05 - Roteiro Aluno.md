# Lab 05: AutoML Nativo (Gemini + Scikit-Learn)
**Disciplina:** Augmented Analytics & AI-Driven Insights
**Objetivo:** Criar um modelo preditivo de alta performance (Evasão/Churn) usando a IA para escrever o próprio pipeline de Ciência de Dados.

---

### 1. O Conceito de Augmented Machine Learning
Neste Lab, você verá o ápice do "Augmented Analytics": em vez de usar uma ferramenta de cliques, você usará um Agente de IA que desenha e executa um pipeline completo de Machine Learning (tratamento de dados, treino de modelo e avaliação de resultados).

### 2. Instruções de Execução
1. Abra o [Google Colab](https://colab.research.google.com/).
2. No menu lateral (ícone de pasta), faça o upload do arquivo: `Lab 05 - EvasaoClientesClassificados.xlsx`.
3. Importe o notebook fornecido pelo professor (`Lab 05 - Colab Notebook.ipynb`).
4. Insira sua **API Key** do Google AI Studio na variável `API_KEY`.

### 3. O Desafio Analítico
Use a função `executar_automl_nativo()` para treinar seu modelo. Você pode passar perguntas de negócio como parâmetro:

*   **Treinamento Básico:** `executar_automl_nativo("Crie o modelo e me diga a acurácia.")`
*   **Análise de Insights:** `executar_automl_nativo("Identifique as 3 variáveis que mais influenciam a saída do cliente.")`
*   **Decisão de Negócio:** `executar_automl_nativo("O nível de cobertura influencia no Churn? Mostre-me via dados.")`

### 4. Reflexão para o Board
*   Observe como a IA executou sozinha as fases de "Preparação" e "Modelagem" do CRISP-DM.
*   A acurácia do modelo é suficiente para uma decisão estratégica de milhões de reais?
*   Qual a vantagem de usar o Gemini para escrever o código (transparência) em vez de uma ferramenta de "caixa preta" (opacidade)?

---
*Dica: Você pode pedir para a IA comparar diferentes modelos! Ex: executar_automl_nativo("Compare a Random Forest com uma Regressão Logística e escolha a melhor.")*
