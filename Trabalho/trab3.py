import pandas as pd
from statistics import mode, median

class CalculadoraEstatistica:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def calcular_estatisticas(self, colunas):
        estatisticas = {}
        for coluna in colunas:
            if coluna in self.dataframe.columns:
                valores = self.dataframe[coluna]
                estatisticas[coluna] = {
                    'moda': mode(valores),
                    'mediana': median(valores),
                    'media': valores.mean()
                }
            else:
                print(f"A coluna '{coluna}' não existe no DataFrame.")

        return estatisticas

# Exemplo de uso:
caminho_arquivo = 'arquivo.csv'  # Substitua pelo caminho do seu arquivo CSV
df = pd.read_csv(caminho_arquivo)

# Criar objeto da calculadora estatística
calculadora = CalculadoraEstatistica(df)

# Calcular estatísticas para as colunas especificadas
colunas_para_calcular = ['Resultado', 'Kcal', 'Carb']
resultado_estatisticas = calculadora.calcular_estatisticas(colunas_para_calcular)

# Exibir resultados
for coluna, estatisticas in resultado_estatisticas.items():
    print(f"Estatísticas para '{coluna}':")
    print(f"Moda: {estatisticas['moda']}")
    print(f"Mediana: {estatisticas['mediana']}")
    print(f"Média: {estatisticas['media']}")
    print()
