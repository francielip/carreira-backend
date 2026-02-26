### Curso: Praticando Python: condicionais if, elif e else

def menu_prinpical():
    print('1. Exercício 01 - Criando um dicionários')
    print('2. Exercício 02 - Calculando o tempo total do projeto')
    print('3. Exercício 03 - Temperatura dos servidores')
    print('4. Exercício 04 - Calculando IMC')
    print('5. Exercício 05 - Controle de orçamento mensal')
    print('6. Exercício 06 - Controle de acesso ao escritório')
    print('7. Exercício 07 - Classificando estudantes por média')

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

def exercicio_05():
    limite = 3000.0
    despesas = float(input('Digite o total de despesas do mês (R$): '))
    if despesas > limite:
        print('Atenção! Você ultrapassou o limite do orçamento.')
    else:
        print('Você ainda está dentro do orçamento.')

def exercicio_06():
    inicio = 8
    fim = 18
    hora_atual = int(input('Digite a hora atual (formato 24hrs): '))
    if hora_atual >= inicio and hora_atual <= fim:
        print('Acesso liberado.')
    elif hora_atual > 0 and hora_atual < inicio:
        print('Acesso negado.')
    elif hora_atual > fim and hora_atual <= 24:
        print('Acesso negado.')
    elif hora_atual > 0 or hora_atual > 24:
        print('Escolha uma hora válida.')    

def exercicio_07():
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    media = sum(nota1,nota2,nota3) / 3
    if media >= 7:
        print(f'Sua média é {media}. Você está aprovado!')
    elif media <= 5 and media < 7:
        print(f'Sua média é {media}. Você está de recuperação.')
    elif media < 5:
        print(f'Sua média é {media}. Você foi reprovado...')


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
    if opcao_escolhida == 5:
        exercicio_05()
    if opcao_escolhida == 6:
        exercicio_06()
    if opcao_escolhida == 7:
        exercicio_07()

def main():
    menu_prinpical()
    escolher_exercicio()

if __name__ == '__main__':
    main()