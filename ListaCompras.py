lista_de_compra = [] # lista vazia para armazenar

while True:
    print('\nEscola uma opção: ')
    print('1 - Adicionar produto')
    print('2 - Apagar produto')
    print('3 - Listar produtos')
    print('4 - Sair')

    opcao = input('Opção: ')

    if opcao == '1':
        produto = input('Digite o produto para adicionar: ')
        lista_de_compra.append(produto)
        print(f'{produto} foi adicionado à lista de compras.')

    elif opcao == '2': # apagar o produto
        if not lista_de_compra:
            print('A lista está vazia. Não há nada para remover. ')
        else:
            try:
                indice = int(input('Digite o índice do produto que deseja apagar: '))
                if 0 <= indice < len(lista_de_compra):
                    produto_removido = lista_de_compra
                    print(f'{produto_removido} foi removido com sucesso da lista de compras. ')
                else:
                    print('Índice inválido. ')
            except ValueError:
                    print('Por favor, digite um número válido: ')

    elif opcao == '3': # listar produtos
        if not lista_de_compra:
            print('A lista de compras está vazia.')
        else: 
            print('\nLista de compras: ')
            for indice, produto in enumerate(lista_de_compra):
                print(f'{indice}: {produto}')
        
    
    elif opcao == '4':
        print('Encerrando o programa...')
        break

    else:
        print('Opção inválida. Por favor, escolha uma opção entre 1 a 4. ')
