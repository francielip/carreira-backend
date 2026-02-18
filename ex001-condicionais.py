### Curso: Python: crie a sua primeira aplicação

# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

print('\n##### Exercício 01 #####')
print('>>> Número par ou ímpar.\n')
numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print(f'O número {numero} é par.')
else:
    print(f'O número {numero} é ímpar.')

# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

print('\n##### Exercício 02 #####')
print('>>> Criança, adolescente ou adulto?\n')
idade = int(input('Digite a sua idade: '))
if 0 < idade <= 12:
    print("Criança")
elif 12 < idade < 18:
    print("Adolescente")
elif idade >= 18:
    print("Adulto")
else: 
    print("Valor inválido!")

# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

print('\n##### Exercício 03 #####')
print('>>> Usuário e senha.\n')
usuario = 'admin'
senha = '123'

usuario_informado = input('Informe o usuario: ')
senha_informado = input('Informe a senha: ')

if usuario_informado == usuario and senha_informado == senha:
    print('Credenciais válidas.')
else:
    print('Credenciais inválidas.')

# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

print('\n##### Exercício 04 #####')
print('>>> Coordenadas.\n')

coordenada_x = float(input('Informe a coordenada X: '))
coordenada_y = float(input('Informe a coordenada Y: '))

if coordenada_x > 0 and coordenada_y > 0:
    print("O ponto está no primeiro quadrante.")
elif coordenada_x < 0 and coordenada_y > 0:
    print("O ponto está no segundo quadrante.")
elif coordenada_x < 0 and coordenada_y < 0:
    print("O ponto está no terceiro quadrante.")
elif coordenada_x > 0 and coordenada_y < 0:
    print("O ponto está no quarto quadrante.")
else:
    print("O ponto está sobre um eixo ou na origem.")