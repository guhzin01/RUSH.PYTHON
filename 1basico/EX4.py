"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

try:
    Numero = int(input("Digite um numero inteiro: "))
    if Numero % 2 == 0:
        print("o numero e par")
    else:
        print("o numero e impar")

except:
    print("o valor nao e inteiro")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = int(input("q horas sao?: "))

dia = range(1, 11)
tarde = range(12, 18)
noite = range(18, 23)

if horario in dia:
    print("bom dia")
elif horario in tarde:
    print("boa tarde")
elif horario in noite:
    print("boa noite")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""


nome = input('digite seu nome: ')
nome_digitos = len(nome)

if nome_digitos <= 4:
    print('seu nome é curto')
elif nome_digitos >=5 and nome_digitos <= 6:
    print('seu nome é normal')
else:
    print('Seu nome é muito grande')