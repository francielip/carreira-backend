# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print(f'O número {numero} é par.')
else:
    print(f'O número {numero} é ímpar.')

# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

idade = int(input('Digite a sua idade: '))
if idade 