📌 Projeto: Previsão de Vendas com Séries Temporais Usando Suavização Exponencial
🎯 Objetivo do Projeto
O projeto tem como objetivo prever o total de vendas para janeiro de 2024 utilizando uma abordagem baseada em séries temporais e o modelo de Suavização Exponencial Simples (SimpleExpSmoothing). A ideia central é identificar padrões nos dados históricos de vendas ao longo de 2023 e, com isso, gerar uma previsão confiável para apoiar decisões estratégicas do negócio.

🔍 Definição do Problema de Negócio
Pergunta-chave:
👉 "Usando dados históricos das vendas ao longo de 2023, seria possível prever o total de vendas em janeiro de 2024?"

A previsão de vendas é uma ferramenta fundamental para:

Planejamento de estoque e produção
Definição de metas e orçamentos
Análise de desempenho e crescimento
Antecipação de possíveis quedas ou picos de demanda

🛠️ Metodologia Utilizada
O projeto foi desenvolvido em etapas claras e organizadas:

1️⃣ Carregamento e pré-processamento dos dados:

Leitura do dataset.
Conversão da coluna de datas para o tipo datetime.
Transformação do DataFrame em uma série temporal com frequência diária (asfreq('D')).
2️⃣ Análise Exploratória de Dados (EDA):

Geração de gráficos para visualização da série temporal.
Criação de uma versão personalizada do gráfico, com estilo de contraste e cores destacadas para uma melhor análise visual.
3️⃣ Aplicação da Suavização Exponencial:

Explicação detalhada sobre o modelo SimpleExpSmoothing.
Definição do parâmetro de suavização (alpha = 0.2).
Treinamento do modelo e extração da série suavizada.
4️⃣ Visualização do Modelo:

Comparação gráfica entre a série original de vendas e a versão suavizada ajustada pelo modelo.
5️⃣ Deploy e Previsão:

Realização da previsão para janeiro de 2024 (1 passo à frente).
Apresentação do valor previsto arredondado para quatro casas decimais.
🔬 Técnica Utilizada: Suavização Exponencial
A técnica de suavização exponencial dá mais peso para dados recentes, diminuindo exponencialmente a influência dos valores antigos. Esse método é particularmente útil para séries temporais sem tendências ou sazonalidade acentuada.

✔️ Parâmetro de Suavização (Alpha):

0.2: Dá mais relevância aos dados recentes, mas ainda mantém uma leve influência dos dados antigos para manter a estabilidade da previsão.
✔️ Justificativa da técnica:

Fácil de implementar e interpretar.
Boa performance para previsões de curto prazo.
Ajuda a reduzir ruídos e flutuações de curto prazo.
📈 Resultados e Conclusões
🔹 Gráficos e comparações: A série suavizada apresentou menor variação e maior estabilidade visual em relação à série original, facilitando a interpretação dos dados.

🔹 Previsão final: O modelo retornou uma previsão de vendas para janeiro de 2024 com um valor aproximado de round(previsoes[0], 4) (substituir pelo valor gerado).

🔹 Conclusão: O modelo de suavização exponencial simples foi capaz de fornecer uma previsão inicial razoável, mas poderia ser melhorado ao considerar modelos mais avançados, como Holt-Winters (para capturar tendências e sazonalidade) ou ARIMA/SARIMA (para séries mais complexas).

🔧 Possíveis Melhorias e Extensões
Testar diferentes valores de alfa e comparar o impacto nas previsões.
Adicionar decomposição da série temporal para avaliar tendências e sazonalidade.
Explorar modelos mais avançados (Holt-Winters, ARIMA, Prophet) para comparar desempenho.
Automatizar o pipeline e transformar o código em uma função reutilizável para novos dados.
Publicar o projeto no GitHub com um README.md bem estruturado.
