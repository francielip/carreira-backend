# Projeto para aplicativo de entrega de comida
import os

# Criação da lista de restaurantes
# restaurantes = ['Casa do Pão','Espetinhos do João','Sucos da Vale']

# Criação de dicionário de restaurantes
restaurantes = [{'nome':'Casa do Pão','categoria':'Japonesa','ativo':False},
                {'nome':'Espetinhos do João','categoria':'Brasileira','ativo':True},
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
    print('3. Alternar estado restaurante')
    print('4. Sair\n')
    # Quebra de linha usando \n

def finalizar_app():
    exibir_subtitulo('Finalizando o app.')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal.')
    main()

def exibir_subtitulo(texto):
    os.system('clear')
    linha = '*' * (len(texto) + 1)
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    # Uma das regras de negócio é todo novo restaurante estar como ativo = False
    dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}
    # Para adicionar o restaurante à lista, usamos append
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso.')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes cadastrados')
    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    # Estrutura de repetição com for
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        # Ternário
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        # Identação com ljust
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    # Ainda não encontrei o restaurante, ele inicia como Falso
    restaurante_encontrado = False
    # Para cada restaurante dentro do dicionário
    for restaurante in restaurantes:
        # Se o nome do restaurante foi encontrado...
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            # Inverte o estado
            restaurante['ativo'] = not restaurante['ativo']
            # Ternário
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso.' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso.'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')

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
            alternar_estado_restaurante()
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