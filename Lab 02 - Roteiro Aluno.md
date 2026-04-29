# Lab 02: O Analista Programável (Python + API)
**Disciplina:** Augmented Analytics & AI-Driven Insights
**Objetivo:** Automatizar a análise financeira de múltiplas startups e gerar relatórios executivos em escala usando Python e a API do Gemini.

---

### 1. Preparação do Ambiente
1. Acesse o [Google Colab](https://colab.research.google.com/).
2. Na janela inicial, selecione a aba **"Upload"** e escolha o arquivo: `Lab 02 - Colab Notebook.ipynb`.
3. No menu lateral esquerdo (ícone de pasta), faça o upload do dataset: `Lab 02 - 50_Startups.csv`.

### 2. Obtendo sua Credencial (API Key)
Para que o código funcione, você precisa de uma chave de acesso:
1. Vá ao [Google AI Studio](https://aistudio.google.com/).
2. No menu lateral, clique em **"Get API Key"**.
3. Clique em **"Create API key in new project"**.
4. Copie a chave gerada (você a colará no código a seguir).

### 3. Execução do Código
**Atenção:** No notebook aberto, localize a célula de configuração da API Key e substitua pelo valor da sua chave:
`API_KEY = 'COLE_SUA_API_KEY_AQUI'`

**Nota:** O laboratório utiliza o motor **Gemini 2.5 Flash** (ou Gemini 3 Flash Preview) para análise de alta performance. Execute as células em sequência.

### 4. O Desafio de Negócio (Venture Capital)
Imagine que você é sócio de um fundo de investimento. O código enviará os dados das startups para a IA com as seguintes missões:
1. **Identificar Eficiência:** Qual startup transforma melhor investimento em P&D em Lucro?
2. **Análise de Gastos:** Onde estão os gargalos administrativos que corroem a margem?
3. **Recomendação Série A:** Justificar qual empresa deve receber o próximo aporte financeiro.

### 5. Reflexão Pós-Execução
Após rodar o script e ver o relatório gerado, discuta com seu grupo:
* Como a IA conseguiu interpretar a "saúde financeira" da tabela sem que você precisasse criar fórmulas no Excel?
* Qual seria a dificuldade de repetir esse processo para 1.000 startups usando o método tradicional (Manual/Dashboard)?
* O relatório gerado é confiável o suficiente para ser enviado a um comitê de investimentos?

---
*Dica: Tente alterar o parâmetro `temperature` no código para 0.9 e observe como a recomendação de investimento se torna mais ousada e criativa.*
