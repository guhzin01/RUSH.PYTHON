nome = input("Digite um nome: ")
procurar = input("Digite o que deseja achar: ")

if procurar in nome:
    print(f"{procurar} esta no nome {nome}")
else:
    print(f"{procurar} nao esta no nome {nome}")