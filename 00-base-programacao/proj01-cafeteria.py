# Desafio: Inventário da Cafeteria (Versão Terminal)
# Passo 1: Criar a lista: estoque = ['cafe', 'bolo', 'pao de queijo']
# Passo 2: Criar a função consultar_item(nome) que retorna se tem ou não no estoque.
# Passo 3: Fazer o loop while que pergunta o item e só para se você digitar "sair".

print('Inventário da Cafeteria Doce Sabor')

# criar a lista
estoque = ['cafe', 'bolo', 'pao de queijo']


# criar a função
def consultar_item(item,estoque):
    if item in estoque:
        return True
    else:
        return False


# criar o loop while
while True:
    print(f'Segue os itens existentes no estoque:\n {estoque}')
    item = input('Informe o item que deseja adicionar ao estoque: ').lower()
    if item == "sair":
        break
    else:
        if consultar_item(item,estoque):
            print('O item digitado já existe no estoque.')
        else:
            print('O item não existe no estoque.')
            estoque.append(item)
            print('Item adicionado ao estoque')