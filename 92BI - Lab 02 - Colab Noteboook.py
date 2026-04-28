# ==============================================================================
# LAB 02: Augmented Analytics com Python e Gemini API
# Objetivo: Automação de Análise Financeira de Startups (Venture Capital)
# Disciplina: Augmented Analytics & AI-Driven Insights
# ==============================================================================

# 1. Instalação da biblioteca oficial do Google Generative AI
!pip install -q -U google-generativeai

import google.generativeai as genai
import pandas as pd
import io

# 2. Configuração da API Key
# INSTRUÇÃO: Substitua 'COLE_SUA_API_KEY_AQUI' pela chave gerada no Google AI Studio
API_KEY = 'COLE_SUA_API_KEY_AQUI'
genai.configure(api_key=API_KEY)

# 3. Carregamento do Dataset (50_Startups.csv)
# Certifique-se de ter feito o upload do arquivo para a pasta 'content' do Colab
try:
    df = pd.read_csv('7BIR - Lab 02 - 50_Startups.csv')
    print("✅ Dataset carregado com sucesso!")
    print(f"Total de registros: {len(df)}")
except FileNotFoundError:
    print("❌ Erro: Arquivo '50_Startups.csv' não encontrado. Faça o upload no menu lateral.")

# 4. Preparação do "Prompt Estratégico"
# Selecionamos uma amostra dos dados para enviar como contexto para a IA
# O formato Markdown ajuda a IA a entender a estrutura da tabela
dados_amostra = df.head(15).to_markdown()

system_instruction = """
Você é um Sócio Sênior de um fundo de Venture Capital (VC). 
Sua especialidade é identificar eficiência operacional em startups de tecnologia. 
Analise os dados financeiros fornecidos e gere um relatório executivo focado em ROI.
"""

prompt_usuario = f"""
Com base na tabela de dados abaixo (amostra de 15 startups), realize as seguintes tarefas:

1. **Análise de Eficiência:** Identifique qual startup apresenta a melhor relação entre 
   investimento em R&D (Pesquisa e Desenvolvimento) e Lucro (Profit).
2. **Diagnóstico de Gastos:** Existe alguma correlação visível entre altos gastos com 
   Administração e a queda na margem de lucro?
3. **Recomendação de Board:** Escolha a startup que você recomendaria para um aporte de 
   Série A e justifique com números reais da tabela.

DADOS DAS STARTUPS:
{dados_amostra}

FORMATAÇÃO: Use negrito para KPIs e tabelas Markdown se necessário.
"""

# 5. Execução da Chamada de IA (Modelo Gemini 1.5 Flash ou Gemini 3 Flash Preview)
model = genai.GenerativeModel(
    model_name="gemini-3-flash-preview",
    system_instruction=system_instruction
)

# Configuração de parâmetros técnicos (Top-P baixo para precisão analítica)
generation_config = {
  "temperature": 0.3,
  "top_p": 0.2,
  "top_k": 40,
  "max_output_tokens": 2048,
}

print("\n🤖 O Agente de IA está analisando os dados... Por favor, aguarde.\n")

response = model.generate_content(
    prompt_usuario,
    generation_config=generation_config
)

# 6. Exibição do Relatório de Insights
print("-" * 80)
print("📊 RELATÓRIO ESTRATÉGICO DE INVESTIMENTO")
print("-" * 80)
print(response.text)
