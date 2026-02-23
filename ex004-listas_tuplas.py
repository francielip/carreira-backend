### Curso: Praticando Python: listas e tuplas

def menu_prinpical():
    print('1. Exercício 01 - Verificando itens na despensa')
    print('2. Exercício 02 - Organizando notas de um concurso de redação')
    print('3. Exercício 03 - Registrando voluntários para uma campanha')
    print('4. Exercício 04 - Unindo o relatório de estoques')
    print('5. Exercício 05 - Reorganizando uma lista de convidados')
    print('6. Exercício 06 - Ordenando os eventos')
    print('7. Exercício 07 - Corrigindo posições na lista de uma corrida de atletismo')
    print('8. Exercício 08 - Removendo o último item de um pedido')
    print('9. Exercício 09 - Calculando a média de notas')
    print('10. Exercício 10 - Registrando dados de alunos')

def exercicio_01():
    lista = ("Pão","Leite","Água")
    item = input('Digite o item que você quer verificar: ')
    if item in lista:
        print('Item já está na lista.')
    else:
        print(f'O item {item} precisa ser comprado.')
    print(lista)

def exercicio_02():
    notas = [85,70,90,60,75]
    print(f'Notas originais: {notas}')
    notas.sort()
    print(f'Notas ordenadas: {notas}')

def exercicio_03():
    # Dessa forma, eu aceitaria somente um voluntário, não é isso que queremos no exercício
    # Por isso usamos While e não somente if
    # voluntarios = []
    # voluntario = input('Digite o nome do voluntário (ou SAIR para encerrar): ')
    # if voluntario != 'SAIR':
    #    voluntarios.append(voluntario)
    #    print(f'Voluntários registrados: {voluntarios}')
    #else:
    #    print('Saindo do sistema...')
    voluntarios = []

    while True:
        nome = input("Digite o nome do voluntário (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        voluntarios.append(nome)  

    print("\nVoluntários registrados:", voluntarios)

def exercicio_04():
    estoque1 = tuple(input("Produtos do estoque 1 (separados por vírgula): ").split(", "))
    estoque2 = tuple(input("Produtos do estoque 2 (separados por vírgula): ").split(", "))
    estoque_combinado = estoque1 + estoque2  
    print(f"Estoque combinado:\n{estoque_combinado}")

def exercicio_05():
    convidados = ['Ana','Pedro','Carlos']
    print(f"Lista atual de convidados: {convidados}")
    novo_convidado = input("Digite o nome do novo convidado: ")
    posicao = int(input("Digite a posição na qual deseja inserir o convidado: "))
    convidados.insert(posicao - 1, novo_convidado)  
    print(f"Lista atualizada de convidados: {convidados}")

def exercicio_06():
    eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']
    eventos_registrados.reverse()
    print(f"Ordem corrigida: {eventos_registrados}")

def exercicio_07():
    resultados = ["Ana", "Carlos", "Pedro"]
    print("Lista original:", resultados)

    erro = input("Digite o nome incorreto: ")
    if erro in resultados:
        correto = input("Digite o nome correto: ")
        posicao = resultados.index(erro)
        resultados.remove(erro)
        resultados.insert(posicao, correto)
        print(f"O nome {erro} foi substituído por {correto}.")
        print("Lista atualizada:", resultados)
    else:
        print("Nome não encontrado.")

def exercicio_08():
    pedidos = input("Pedidos feitos (separados por vírgula): ").split(", ")
    pedidos.pop()
    print("Pedidos finais:")
    print(pedidos)

def exercicio_09():
    notas = input("Digite as notas dos alunos separadas por vírgula: ").split(",")
    notas = [float(nota.strip()) for nota in notas]
    media = sum(notas) / len(notas)
    print(f"Média final da turma: {media:.2f}")

def exercicio_10():
    dados = input("Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ").split(", ")
    for i in range(0, len(dados), 3):
        nome, idade, nota = dados[i], int(dados[i + 1]), float(dados[i + 2])
        print(f"Aluno: {nome}")
        print(f"Idade: {idade}")
        print(f"Nota: {nota}\n")


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
    if opcao_escolhida == 8:
        exercicio_08()
    if opcao_escolhida == 9:
        exercicio_09()
    if opcao_escolhida == 10:
        exercicio_10()

def main():
    menu_prinpical()
    escolher_exercicio()

if __name__ == '__main__':
    main()