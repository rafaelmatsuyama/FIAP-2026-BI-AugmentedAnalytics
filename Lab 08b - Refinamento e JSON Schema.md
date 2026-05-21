# Lab 08b: Refinamento e JSON Schema (AI Studio)

## 🏢 1. Contexto Executivo (Business Case)
No mundo corporativo, a IA não pode ser "imprevisível". Se um sistema de BI (como o Dashboard que você criou no Lab 08a) espera um número, a IA não pode responder com um texto longo. 

Neste laboratório, você aprenderá a **domar a IA**. Vamos configurar o "Cérebro" do seu Agente no **Google AI Studio** para garantir que ele sempre responda no formato exato que seu sistema precisa, com o tom de voz de um consultor sênior da FIAP.

---

## 🎯 2. Entregáveis Técnicos
1.  **System Instruction:** Uma "Constituição" para o seu Agente (regras de comportamento).
2.  **JSON Schema:** Uma estrutura rígida de dados que impede a IA de alucinar no formato.
3.  **Prompt Testado:** Validação de como o modelo se comporta com diferentes níveis de "Criatividade" (Temperature).

---

## 🚀 3. Passo a Passo: Configurando o Cérebro da IA

### Passo 1: Acesso ao Google AI Studio
1.  **Acesse:** [aistudio.google.com](https://aistudio.google.com)
2.  **Login:** Use sua conta Google habitual.
3.  **Novo Prompt:** Clique em **"Create New"** > **"Chat prompt"**.

### Passo 2: Definindo a "Constituição" (System Instructions)
No campo superior esquerdo (**System Instructions**), cole e adapte o seguinte texto:
> "Você é um Consultor Estratégico do MBA em BI & Analytics da FIAP. Seu tom é pragmático, focado em ROI e métricas. 
> Regras: 
> 1. Nunca responda com 'Eu acho'. Use 'Baseado nos dados'.
> 2. Todas as recomendações devem ter uma estimativa de impacto (Baixo, Médio, Alto).
> 3. Seja direto e evite introduções desnecessárias."

### Passo 3: Forçando o Formato de Dados (JSON Schema)
Agora vamos garantir que a IA responda em um formato que um computador entenda.
1.  No menu lateral direito, procure por **"Structured Output"**.
2.  Ative a opção (Toggle ON) e clique no botão **"Edit"**.
3.  Defina os campos que você deseja que a IA preencha (Título do Insight, Valor da Métrica, Recomendação).
    - *Dica:* No campo `impacto_estimado`, utilize o tipo **Enum** com os valores `["Baixo", "Médio", "Alto"]`. Isso garante que a IA não invente novos níveis de impacto e seu dashboard exiba as cores corretamente.
    - *Dica:* Isso garante que a IA sempre entregue uma tabela "invisível" que alimenta seu Dashboard.

### Passo 4: Teste de Stress (O Laboratório)
Utilize o dataset `PesquisaClientes.csv` (fornecido na Aula 01) como base para o teste de stress:
1.  Abra o arquivo `PesquisaClientes.csv` no seu computador e copie as primeiras 5 a 10 linhas de dados.
2.  Cole no campo de chat do AI Studio com o seguinte comando:
    - *"Analise os seguintes dados de pesquisa e gere um insight estratégico seguindo o formato JSON definido."*
3.  Observe como a IA agora responde **apenas o JSON estruturado**, sem "conversinha".
4.  **Desafio:** Tente mudar a **Temperature** (no menu lateral) para `1.5` e depois para `0.1`. Veja como a IA se torna mais "doida" ou mais "robótica/precisa".

---

## ⚠️ 4. Dicas de Ouro para Negócios
-   **JSON é a linguagem das máquinas:** Ao aprender isso, você fala a mesma língua que os desenvolvedores da sua empresa.
-   **System Instructions são o RH da IA:** É aqui que você define se sua IA será um estagiário criativo ou um diretor rigoroso.

---
*Material desenvolvido para o MBA em BI & Analytics - FIAP.*