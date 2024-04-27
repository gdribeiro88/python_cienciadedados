from google.colab import drive
drive.mount('/content/drive')
import pandas as pd


#carregar arquivo em dataframe
arquivo = "/content/pandas/glicose_data_suja (1).csv"
df = pd.read_csv(arquivo)

print(df)

# Função para verificar e remover inconsistências
def verificar_e_remover_inconsistencias(df):
    # Aqui você pode adicionar as regras de validação de acordo com sua necessidade
    inconsistencias = []

    # Verificar e remover registros com valores nulos
    df_sem_nulos = df.dropna()
    
    # Verificar se houve registros removidos
    if len(df_sem_nulos) < len(df):
        inconsistencias.append(f"{len(df) - len(df_sem_nulos)} registros com valores nulos foram removidos.")
    
    # Adicione mais verificações conforme necessário...

    return df_sem_nulos, inconsistencias


# Verificar e remover inconsistências
df_sem_inconsistencias, inconsistencias = verificar_e_remover_inconsistencias(df)

# Exibir resultados
if len(inconsistencias) > 0:
    print("Foram encontradas as seguintes inconsistências:")
    for inconsistencia in inconsistencias:
        print("- ", inconsistencia)
    print("Os registros com inconsistências foram removidos.")
    # Aqui você pode salvar o DataFrame sem inconsistências em um novo arquivo CSV se desejar:
    # df_sem_inconsistencias.to_csv('arquivo_sem_inconsistencias.csv', index=False)
else:
    print("Não foram encontradas inconsistências no arquivo CSV.")



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

# Criar objeto da calculadora estatística
calculadora = CalculadoraEstatistica(df)

# Calcular estatísticas para as colunas especificadas
colunas_para_calcular = ['Resultado', 'kcal', 'carb']
resultado_estatisticas = calculadora.calcular_estatisticas(colunas_para_calcular)

# Exibir resultados
for coluna, estatisticas in resultado_estatisticas.items():
    print(f"Estatísticas para '{coluna}':")
    print(f"Moda: {estatisticas['moda']}")
    print(f"Mediana: {estatisticas['mediana']}")
    print(f"Média: {estatisticas['media']}")
    print()
