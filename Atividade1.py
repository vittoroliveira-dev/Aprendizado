nome = str(input('Digite o seu nome: '))

if not nome.strip(): # verifica se a string está vazia ou contém apenas espaços
    print('Nada foi digitado para o nome.')
else:
    print(f'Seu nome é {nome}')

idade = input('Digite sua idade: ')

if not idade.strip(): # verifica se foi digitado alguma coisa
    print('Nada foi digitado para a idade.')
else:
    try:
        idade = int(idade) # converte para inteiro
        print(f'Sua idade é: {idade}')
    except ValueError:
        print('A idade precisa ser um número válido.')

# inversão de nome
print(f'Seu nome invertido é:', nome[::-1])

# verifica se contém espaços
if " " in nome:
    print('Seu nome contém espaço.')
else:
    print('Seu nome não contém espaços.')

# quantidade de letras no nome
print('Quantidade de letras em seu nome:',(len(nome)))

# primeira e última letra do nome
primeira_letra = nome[0]
ultima_letra = nome[-1]

print(f'A primeira letra é: {primeira_letra}')
print(f'A última letra é: {ultima_letra}')
