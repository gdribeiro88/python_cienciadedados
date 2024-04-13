nome = input("Digite seu nome")

print(nome)

nome = nome.upper()

vetor_nomes = nome.split(" ")

print("Primeiro nome ", vetor_nomes[0])
print("Sobrenome ", vetor_nomes[-1])