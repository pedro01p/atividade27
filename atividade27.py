# Solicite ao usuário que insira o nome de até 7 convidados.
# Armazene os nomes em uma lista.
# Permita ao usuário remover um convidado da lista, caso necessário.
# Exiba a lista final de convidados.

# Digite o nome do convidado 1: João
# Digite o nome do convidado 2: Maria
# ...
# Digite o nome do convidado 7: Pedro
# Deseja remover algum convidado da lista? (sim/não): sim
# Digite o nome do convidado a ser removido: Maria

lista=[]
sans = str("o")

for c in range(7):
    convidado = input(F"digite o nome do {c + 1} convidado")
    lista.append (convidado)
    
    if c == 6:
        sans=input("deseja remover algum convidado? (sim/não)")
if sans == "sim":
    rmv = str(input("Digite o nome do convidado que deseja remover: "))
    lista.remove(rmv)
    print(lista)
elif sans == "nao":
    print("poixta")