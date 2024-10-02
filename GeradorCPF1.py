import random

# Função para calcular o dígito verificador com base na soma ponderada
def calcular_digito(soma):
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

# Função para gerar CPF válido
def gerar_cpf():
    # Gerando os 9 primeiros dígitos aleatórios
    cpf = [random.randint(0, 9) for _ in range(9)]
    
    # Cálculo do primeiro dígito verificador
    soma1 = sum(cpf[i] * (10 - i) for i in range(9))
    primeiro_digito = calcular_digito(soma1)

    # Cálculo do segundo dígito verificador
    soma2 = sum(cpf[i] * (11 - i) for i in range(9)) + primeiro_digito * 2
    segundo_digito = calcular_digito(soma2)

    # Adicionando os dígitos verificadores ao CPF
    cpf.append(primeiro_digito)
    cpf.append(segundo_digito)

    # Formatando o CPF em string
    cpf_formatado = f"{cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]}"
    return cpf_formatado

# Função para rodar o sistema de menu
def menu():
    lista_cpf = []

    while True:
        print('\nEscolha uma opção: ')
        print('1 - Gerar um CPF')
        print('2 - Listar CPFs')
        print('3 - Sair')

        opcao = input('Opção: ')

        if opcao == '1':
            cpf_gerado = gerar_cpf()
            lista_cpf.append(cpf_gerado)
            print(f'{cpf_gerado} foi adicionado à lista de CPFs.')

        elif opcao == '2':
            print('CPFs gerados:')
            for cpf in lista_cpf:
                print(cpf)

        elif opcao == '3':
            break

        else:
            print('Opção inválida, tente novamente.')

menu()
