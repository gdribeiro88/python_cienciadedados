from oo1 import Glicemia
import os

# Imprime o diretório de trabalho atual
print("Diretório de trabalho atual:", os.getcwd())

nome_arquivo = "glicose_data_suja.csv"

# Verificar se o arquivo existe
if not os.path.exists(nome_arquivo):
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
else:
    lista_glicemias = []
    # Abrir e capturar as linhas do arquivo
    with open(nome_arquivo, "r", encoding="utf8") as leitor:
        for i, linha in enumerate(leitor, 1):  # Adiciona um contador de linha para ajudar na depuração
            linha = linha.strip()
            if linha:
                vetor_linha = linha.split(",")
                try:
                    obj = Glicemia(vetor_linha[0], vetor_linha[1], vetor_linha[3], vetor_linha[4],
                                   vetor_linha[5], vetor_linha[6], vetor_linha[7])
                    lista_glicemias.append(obj)
                except IndexError:
                    print(f"Erro: Não há dados suficientes na linha {i}.")
                except ValueError as e:
                    print(f"Erro na linha {i}: Um ou mais campos não são numéricos - {e}")
                    print("Linha problemática:", linha)

    # Ordena a lista de objetos Glicemia pela quantidade de carboidratos
    lista_glicemias.sort(key=lambda glicemia: glicemia.carb)

    print("Quantos dados foram capturados? " + str(len(lista_glicemias)))
    for item in lista_glicemias:
        print(item)