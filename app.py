# Projeto para aplicativo de entrega de comida
import os

# Criação da lista de restaurantes
# restaurantes = ['Casa do Pão','Espetinhos do João','Sucos da Vale']

# Criação de dicionário de restaurantes
restaurantes = [{'nome':'Casa do Pão','categoria':'Japonesa','ativo':False},
                {'nome':'Espetinhos do João','categoria':'Brasileira','ativo':True}
                {'nome':'Sucos da Vale','categoria':'Natural','ativo':False}]

# Criando funções com def
def exibir_nome_do_app():
    print("""
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
""")

def menu_prinpical():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')
    # Quebra de linha usando \n

def finalizar_app():
    exibir_subtitulo('Finalizando o app.')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal.')
    main()

def exibir_subtitulo(texto):
    os.system('clear')
    print(texto)
    print()

def opcao_invalida():
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    # Para adicionar o restaurante à lista, usamos append
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso.')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes cadastrados')
    # Estrutura de repetição com for
    for restaurante in restaurantes:
        print(f'- {restaurante}')
    voltar_ao_menu_principal()

def escolher_opcao():
    # Try para controle de execução
    try:
        # Conversão de tipo de string para inteiro usando int()
        opcao_escolhida = int(input('Escolha uma opção: '))
        # Interpolação de strings usando f-strings
        print(f'Voce escolheu a opcao {opcao_escolhida}.')
        # Estrutura condicional usando if, elif e else  
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('clear')
    exibir_nome_do_app()
    menu_prinpical()
    escolher_opcao()

if __name__ == '__main__':
    main()