def menu_prinpical():
    print('1. Exercício 01 - Comparacao de vendas')
    print('2. Exercício 02 - Calculando o tempo total do projeto')
    print('3. Exercício 03 - Temperatura dos servidores')
    print('4. Exercício 04 - Calculando IMC')

def exercicio_01():
    macas = int(input('Digite a quantidade de macas vendidas: '))
    bananas = int(input('Digite a quantidade de bananas vendidas: '))
    if macas > bananas:
        print('As macas tiveram mais vendas.')
    elif macas < bananas:
        print('As bananas tiveram mais vendas.')
    else:
        print('A quantidade vendida foi igual.')

def exercicio_02():
    atividade_a = int(input('Informe os dias para a atividade A: '))
    atividade_b = int(input('Informe os dias para a atividade B: '))
    atividade_c = int(input('Informe os dias para a atividade C: '))
    if (atividade_a >= 0 and atividade_b >= 0 and atividade_c >= 0):
        tempo_total = atividade_a + atividade_b + atividade_c
        print(f"O tempo total do projeto é de {tempo_total} dias.")
    else: 
        print("Erro: Os dias não podem ser negativos.")

def exercicio_03():
    temp_atual = int(input('Digite a temperatura atual: '))
    if temp_atual > 25:
        print('Alerta! Temperatura acima do limite permitido.')
    else:
        print('Temperatura normal.')

def exercicio_04():
    peso = float(input('Digite o seu peso (kg): '))
    altura = float(input('Digite a sua altura (m): '))
    imc = peso / (altura ** 2)
    print(f'Seu IMC é {imc}.\n')
    if imc < 18.5:
        print('Você está abaixo do peso.')
    elif imc <= 18.5 or imc < 25:
        print('Você está com peso normal.')
    else:
        print('Você está acima do peso.')

def escolher_exercicio():
    opcao_escolhida = int(input('Escolha uma opção: '))
    if opcao_escolhida == 1:
        exercicio_01()
    if opcao_escolhida == 2:
        exercicio_02()
    if opcao_escolhida == 3:
        exercicio_03()
    if opcao_escolhida == 4:
        exercicio_04()

def main():
    menu_prinpical()
    escolher_exercicio()

if __name__ == '__main__':
    main()