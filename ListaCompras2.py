import json
import os

# Função para carregar lista de compras de um arquivo JSON
def carregar_lista():
    if os.path.exists('lista_de_compras.json'):
        with open('lista_de_compras.json', 'r') as file:
            return json.load(file)
    return []

# Função para salvar a lista de compras em um arquivo JSON
def salvar_lista(lista):
    with open('lista_de_compras.json', 'w') as file:
        json.dump(lista, file)

# Lista de compras carregada do arquivo
lista_de_compras = carregar_lista()

while True:
    print("\nEscolha uma opção:")
    print("1 - Adicionar produto")
    print("2 - Apagar produto")
    print("3 - Listar produtos")
    print("4 - Sair")
    
    opcao = input("Opção: ")

    if opcao == '1':  # Adicionar produto
        produto = input("Digite o nome do produto para adicionar: ")
        lista_de_compras.append(produto)
        salvar_lista(lista_de_compras)
        print(f"{produto} foi adicionado à lista de compras.")
    
    elif opcao == '2':  # Apagar produto
        if not lista_de_compras:
            print("A lista está vazia. Não há nada para remover.")
        else:
            try:
                indice = int(input("Digite o índice do produto que deseja apagar: "))
                if 0 <= indice < len(lista_de_compras):
                    produto_removido = lista_de_compras.pop(indice)
                    salvar_lista(lista_de_compras)
                    print(f"{produto_removido} foi removido da lista de compras.")
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Por favor, digite um número válido.")
    
    elif opcao == '3':  # Listar produtos
        if not lista_de_compras:
            print("A lista de compras está vazia.")
        else:
            print("\nLista de compras:")
            for indice, produto in enumerate(lista_de_compras):
                print(f"{indice}: {produto}")
    
    elif opcao == '4':  # Sair
        print("Encerrando o programa...")
        break
    
    else:
        print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
