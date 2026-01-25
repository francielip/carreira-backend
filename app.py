# Projeto para aplicativo de entrega de comida
import os

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
    os.system('clear')
    print('Finalizando o app.\n')

def main():
    exibir_nome_do_app()
    menu_prinpical()
    escolher_opcao()

def escolher_opcao():
    # Conversão de tipo de string para inteiro usando int()
    opcao_escolhida = int(input('Escolha uma opção: '))
    # Interpolação de strings usando f-strings
    print(f'Voce escolheu a opcao {opcao_escolhida}.')
    # Estrutura condicional usando if, elif e else  
    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    else:
        finalizar_app()

if __name__ == '__main__':
    main()