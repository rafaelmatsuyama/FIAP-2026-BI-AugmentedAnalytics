# Lab 03: Gabarito & Guia de Discussão (Professor)
**Datasets:** `Lab 01 - PesquisaClientes.csv` & `Lab 02 - 50_Startups.csv`

---

### Conexões Semânticas Esperadas:

1. **Cruzamento de Perfis (O "Pulo do Gato"):**
   * **Insight:** Os alunos devem notar que pessoas mais jovens (Idade < 30) ou com salários menores em `Lab 01 - PesquisaClientes.csv` compram menos.
   * **Sinergia Estratégica:** A IA deve sugerir que, se o problema é conversão de jovens, a empresa deve adquirir uma startup de `Lab 02 - 50_Startups.csv` que invista pesado em **Marketing** (para captar esse público) ou em **R&D** (para criar um produto mais acessível).
   * **Exemplo Real:** *"Minha base atual de clientes é majoritariamente acima de 35 anos. Para atrair o público jovem que não compra (Lab 01 - PesquisaClientes), recomendo adquirir a Startup ID X (Lab 02 - 50_Startups), que possui o maior gasto em Marketing Spend e inovação em R&D."*

2. **Diferença de Modelos (Flash vs. Pro):**
   * No Lab 02 usamos o Flash para velocidade. No Lab 03, o **Gemini 3 Flash Preview** é essencial.
   * **O que observar:** O modelo Pro tende a ser muito mais "argumentativo", criando uma narrativa executiva de M&A que parece escrita por um analista da McKinsey ou BCG.

### Pontos para Discussão em Aula:

* **Raciocínio Cross-Dataset:** Ressalte que o BI tradicional exigiria um "Data Warehouse" e um "Join" entre as tabelas. A IA faz esse cruzamento por **Semântica de Negócio** (sem precisar de chaves estrangeiras ou SQL).
* **Uso de Top-P:** Mostre como o **Top-P em 0.9** torna a IA mais "disruptiva" em suas sugestões, enquanto o **0.2** a mantém conservadora e focada em lucro imediato. Pergunte: *"Qual estilo de conselho sua empresa precisaria hoje?"*.
* **Augmented Analytics:** Este Lab é a prova viva do conceito: a IA aumenta a capacidade humana de processar informações díspares para tomar uma decisão.

---
### Fechamento da Aula:
Use este Lab para mostrar que o futuro do BI & Analytics não é apenas saber "o que aconteceu", mas ser capaz de **orquestrar dados heterogêneos** para responder perguntas de "board level".
