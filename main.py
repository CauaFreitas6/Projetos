# TÍTULO: Previsão de Vendas com Séries Temporais Usando Suavização Exponencial

# ANÁLISE DE SÉRIES TEMPORAIS
# PROBLEMA DE NEGÓCIO:

# USANDO DADOS HISTÓRICOS DAS VENDAS AO LONGO DE 2023 SERIA POSSÍVEL PREVER O TOTAL DE VENDAS EM JANEIRO/2024?

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

# CARREGANDO DADOS

# Carrega o dataset
df_dsa = pd.read_csv('dataset.csv')

print(df_dsa.shape)
print(df_dsa.columns)
print(df_dsa.head())
print(df_dsa.tail())



# PRÉ-PROCESSAMENTO DOS DADOS

# Valor mínimo da coluna data
df_dsa['Data'].min()

# Valor máximo da coluna data
df_dsa['Data'].max()

print(df_dsa.info())

# Converte a coluna de data no tipo datetime
df_dsa['Data'] = pd.to_datetime(df_dsa['Data'])

print(df_dsa.head())
print(df_dsa.info())

# Converter o DataFrame em uma série temporal com a data como índice
serie_temporal = df_dsa.set_index('Data')['Total_Vendas']

print(type(serie_temporal))
print(serie_temporal)

# Fornece a frequência da série temporal (diária, neste caso)
serie_temporal = serie_temporal.asfreq('D')
print(serie_temporal)



# ANÁLISE EXPLORATÓRIA
# Cria o gráfico da série temporal (SEM FORMATAÇÃO)
plt.figure(figsize = (12, 6))
plt.plot(serie_temporal)
plt.xlabel('Data')
plt.ylabel('Vendas')
plt.title('Série Temporal de Vendas')
plt.grid(True)
plt.show()


# Cria o gráfico da série temporal (COM FORMATAÇÃO)

# Criar o gráfico da série temporal com layout de contraste
plt.figure(figsize = (12, 6))
plt.plot(serie_temporal, color = 'white', linewidth = 2)

# Configurar cores e estilo do gráfico
plt.gca().set_facecolor('purple')
plt.grid(color = 'yellow', linestyle = '--', linewidth = 0.5)

# Configurar rótulos dos eixos, títulos e legenda
plt.xlabel('Data', color = 'black', fontsize = 14)
plt.ylabel('Vendas', color = 'black', fontsize = 14)
plt.title('Série Temporal de Vendas', color = 'black', fontsize = 18)

# Configurar as cores dos eixos e dos ticks (marcadores)
plt.tick_params(axis = 'x', colors='black')
plt.tick_params(axis = 'y', colors='black')

plt.show()



# SUAVIZAÇÃO EXPONENCIAL
# A suavização exponencial é uma técnica de análise e previsão de séries temporais que aplica médias ponderadas aos dados históricos, onde os pesos diminuem
#exponencialmente à medida que os dados ficam mais antigos. A suavização exponencial é útil para lidar com tendências e sazonalidades nos dados, e para
#reduzir o ruído.

# Suposições da Suavização Exponencial
# No Statsmodels, a classe SimpleExpSmoothing é uma implementação da técnica de suavização exponencial simples, que é uma versão mais básica da suavização
#exponencial que não lida explicitamente com tendências e sazonalidades.

# O modelo SimpleExpSmoothing do Statsmodels, também conhecido como suavização exponencial simples ou média móvel exponencialmente ponderada, é uma técnica
#de suavização de séries temporais que atribui pesos decrescentes exponencialmente aos pontos de dados passados. Ele é usado principalmente para suavizar
#séries temporais e fazer previsões de curto prazo. As principais suposições do modelo SimpleExpSmoothing são as seguintes:

# - A série temporal é composta por um componente de nível (média) e um componente de erro aleatório (ruído). Não há componentes de tendência ou
#sazonalidade na série.

# - O componente de nível é uma média ponderada dos valores passados, com pesos que diminuem exponencialmente à medida que os dados ficam mais distantes no 
#passado.

# - O componente de erro aleatório é normalmente distribuído com média zero e variância constante. Além disso, os erros são independentes e identicamente
#distribuídos.

# - O parâmetro de suavização (alfa) é uma constante entre 0 e 1, que determina a taxa de decaimento dos pesos. Valores próximos a 1 dão maior peso aos
#dados mais recentes, enquanto valores próximos a 0 dão mais peso aos dados mais antigos.

# O modelo SimpleExpSmoothing é uma técnica de suavização bastante simples que tem suas limitações. Ele é mais adequado para séries temporais que não 
#apresentam tendências ou sazonalidades claras e para fazer previsões de curto prazo. Para séries temporais com componentes de tendência e/ou sazonalidade,
#modelos mais avançados como o ExponentialSmoothing de Holt-Winters ou modelos SARIMA podem ser mais apropriados.



# CONSTRUÇÃO E TREINAMENTO DO MODELO DE SUAVIZAÇÃO EXPONENCIAL

# Cria o modelo
modelo = SimpleExpSmoothing(serie_temporal)
# Esta linha acima cria uma instância da classe SimpleExpSmoothing, utilizando a coluna 'Vendas' da série serie_temporal como entrada.

# Treinamento (ajuste) do modelo
modelo_ajustado = modelo.fit(smoothing_level = 0.2)
# Esta linha acima faz uma chamada ao método fit() para ajustar o modelo de suavização exponencial aos dados. O argumento smoothing_level=0.2 define o
#parâmetro de suavização (alfa) como 0.2. O parâmetro de suavização controle a rapidez com que os pesos decrescem ao longo do tempo; um valor maior
#atribui mais peso aos dados mais recentes, enquanto um valor menor atribui mais peso aos dados mais antigos. O valor de alfa deve estar entre 0 e 1.

# Extrai os valores previstos pelo modelo
suavizacao_exponencial = modelo_ajustado.fittedvalues
# Esta linha acima extrai os valores ajustados do modelo de suavização exponencial. Os valores ajustados são as estimativas da série temporal suavizada, que
#são calculadas aplicando os pesos exponenciais aos dados históricos. Esses valores ajustados podem ser usados para analisar a série temporal suavizada,
#identificar tendências e comparar com outras técnicas de suavização ou previsão.

# O resultado final é uma nova série temporal chamada suavizacao_exponencial, que representa a versão suavizada da série original de vendas, com menos
#ruído e flutuações de curto prazo.

# Plot
plt.figure(figsize = (12, 6))
plt.plot(serie_temporal, label = 'Valores Reais')
plt.plot(suavizacao_exponencial, label = 'Valores Previstos', linestyle = '--')
plt.xlabel('Data')
plt.ylabel('Vendas')
plt.title('Modelo de Suavização Exponencial')
plt.legend()

plt.show()



# DEPLOY E PREVISÃO COM O MODELO TREINADO
# Fazer previsões
num_previsoes = 1
previsoes = modelo_ajustado.forecast(steps = num_previsoes)
print('Previsão do Total de Vendas Para Janeiro/2024:', round(previsoes[0], 4))
 
