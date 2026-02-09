# 1 - Crie uma lista para cada informação a seguir:
# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.
print('\n_____ Exercício 01 _____')
print('>>> Criando listas e exibindo elas\n')
numeros =['1','2','3','4','5','6','7','8','9','10']
nomes = ['Francieli','Ricardo','Leandro']
anos = ['1984','2026']
print(numeros)
print(nomes)
print(anos)

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
print('\n_____ Exercício 02 _____')
print('>>> Criando lista com loop\n')
cores = ['Preto','Branco','Azul']
for cor in cores:
    print(f'Cor: {cor}')

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
print('\n_____ Exercício 03 _____')
print('>>> Loop para calcular a soma dos números impares\n')
soma_impares = 0
for i in range(1,11,2):
    soma_impares += i
print(f'A soma dos numeros impares é {soma_impares}.')

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
print('\n_____ Exercício 04 _____')
print('>>> Loop para mostrar os numeros de 1 a 10 em ordem decrescente\n')
for i in range(10,0,-1):
    print(i)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
print('\n_____ Exercício 05 _____')
print('>>> Loop para exibir a tabuada do número escolhido\n')
numero = int(input('Informe um numero inteiro para calcular: '))
for i in range(1,11):
    tabuada = numero * i
    print(f'{numero} X {i} = {tabuada}')

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
print('\n_____ Exercício 06 _____')
print('>>> Loop para calcular a soma\n')
numeros = [2,4,6,8]
soma = 0
try:
    for numero in numeros:
        soma = soma + numero
    print(f'A soma dos números é: {soma}')
except Exception as e:
    print(f'Ocorreu um erro: {e}')

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
print('\n_____ Exercício 07 _____')
print('>>> Calculando a media dos valores\n')
numeros = [1,2,3,4,5]
soma = 0
try:
    for numero in numeros:
        soma += numero
    media = soma / len(numeros)
    print(f'Média dos valores: {media}')
except ZeroDivisionError:
    print('A lista está vazia, não é possível calcular a média.')
except Exception as e:
    print(f'Ocorreu um erro: {e}') 