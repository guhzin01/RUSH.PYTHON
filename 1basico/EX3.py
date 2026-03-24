nome = input("Digite um nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print(f"seu nome {nome}")
    print(f"seu nome invertido {nome[::-1]}")
    if " " in nome:
        print(f"seu nome tem espacos e tem {len(nome)} caracteres")
        print(f"e a primeira letra e {nome[0]}")
    else:
        print("seu nome nao tem espacos")
else:
    print("um dos campos vazio, tente novamente")





