# Lab 08a: Dashboard de Analytics com Agentes Inteligentes (UI)

## 🏢 1. Contexto Executivo (Business Case)
O BI tradicional é reativo: o usuário precisa abrir um dashboard, filtrar dados e *tentar* extrair conclusões. Neste lab, estamos construindo a evolução: o **Agentic Analytics**. 

Sua missão é criar um protótipo de **"Insight-as-a-Service"**. O usuário final (um Diretor de Marketing ou Vendas) não quer ver gráficos complexos; ele quer fazer o upload de uma planilha e receber uma análise estratégica em linguagem natural, gerada por uma Squad de Agentes de IA especialistas.

---

## 🎯 2. Entregáveis Técnicos
Ao final deste laboratório, você terá construído:
1.  **Interface Web:** Um dashboard funcional criado 100% em Python (Streamlit).
2.  **Motor de Integração:** Um túnel de comunicação entre o Google Colab e a web (Ngrok).
3.  **Conexão Agentic:** O front-end disparando a lógica do CrewAI (desenvolvida na Aula 03).

---

## 🚀 3. Passo a Passo: Acesso e Configuração

### A. Google Colab (Seu Workbench)
1.  **Acesse:** [colab.new](https://colab.new) e faça o upload do notebook `.ipynb` fornecido.
2.  **Configuração:** O notebook já contém as células de instalação das bibliotecas (`crewai`, `streamlit`, `pyngrok`). Execute-as em sequência.

### B. Streamlit Cloud (Sua Hospedagem)
1.  **Acesse:** [share.streamlit.io](https://share.streamlit.io)
2.  **Sign Up:** Selecione **"Continue with Google"**. Utilize sua conta Google habitual.
3.  **Nota:** Embora este laboratório rode "dentro" do Colab para testes rápidos, o cadastro no Streamlit Cloud é o primeiro passo para você publicar seu portfólio no futuro.

### C. Ngrok Token (Sua Ponte de Comunicação)
Como o Streamlit roda em um servidor interno no Colab, o Ngrok gerará a URL pública de acesso.
1.  **Acesse:** [ngrok.com](https://ngrok.com) e crie sua conta grátis.
2.  **Obter Token:** No menu lateral, clique em **"Your Authtoken"** e copie o código (Ex: `2t8X...`).
3.  **Aplicação:** Cole este token na última célula do Notebook para que o link de acesso seja gerado.

---

## 🛠️ 4. Fluxo de Execução do Lab
1.  **Setup de Dependências:** Instalação silenciosa das bibliotecas.
2.  **Escrita do App:** Você executará a célula que gera o arquivo `app.py`. Este arquivo contém o código da interface (botões, sliders, uploader).
3.  **Input de API Key:** Insira sua Gemini API Key diretamente na barra lateral (Sidebar) do Dashboard para garantir a segurança da sua chave.
4.  **Upload & Análise:** Arraste um arquivo CSV (ex: `PesquisaClientes.csv`) e clique em **"Disparar Squad de Agentes"**.

---

## ⚠️ 5. Troubleshooting (Dicas de Sobrevivência)
-   **Erro de API Key:** Se o dashboard der erro, verifique se não há espaços em branco antes ou depois da sua Gemini Key.
-   **Túnel Não Abre:** Se a URL do Ngrok não carregar, pare o runtime do Colab e execute novamente a última célula.
-   **Dataset Não Carrega:** Verifique se o arquivo CSV está usando separador vírgula (padrão Pandas).

---
*Material desenvolvido para o MBA em BI & Analytics - FIAP.*