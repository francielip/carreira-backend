# if: as condições servem para selecionar quando uma pare do programa de ser ativada e quando deve ser simplemente ignorada. No python, a estrutura de decisão é o if.
# tem a estrutura:
# if <condição>:
#   bloco verdadeiro
# Se a condição for verdadeira, faça algo
# Programa 4.1 - Lê dois valores e imprime qual é o maior
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
if a > b:
    print("O primeiro valor é o maior.")
if b > a:
    print("O segundo valor é o maior.")
# a linha com a condição em si é executa mesmo se o resultado da expressão for falso
# Programa 4.2 - Carro novo ou velho, dependendo da idade
idade = int(input("Digite a idade do seu carro: "))
if idade <= 3:
    print("Seu carro é novo.")
if idade > 3:
    print("Seu carro é velho.")
# Exercício 4.2 Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.
velocidade = int(input("Qual a velocidade do seu carro: "))
if velocidade > 80:
    vel_excedente = velocidade - 80
    valor_multa = 5
    multa = vel_excedente * valor_multa
    print(f"Você foi multado! O valor cobrado será de R$ {multa}.")
else:
    print("Parabéns. Você está dentro da velocidade permitida.")
# para melhorar, poderia usar variável tb para o limite de velocidade e melhorar a nomenclatura das variaveis. tb poderia melhorar informando em quantos km ele passou, deixando as mensagens mais claras.
# Programa 4.3 - Cálculo de imposto de renda
salario = float(input("Digite o salário para o cálculo do IR: "))
base = salario
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
print(f"Salário: R$ {salario:.2f}")
print(f"Imposto de Renda: R$ {imposto:.2f}")

# Exercício 4.3 Escreva um programa que leia três números e que imprima o maior e o menor.
num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
num3 = float(input("Informe o terceiro número: "))

maior = num1
menor = num1

if num2 > maior:
    maior = num2
if num2 < menor:
    menor = num2
if num3 > maior:
    maior = num3
if num3 < menor:
    menor = num3

print(f"O menor número é o {menor} e o maior número é o {maior}.")


# Exercício 4.4 Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
