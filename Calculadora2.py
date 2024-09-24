"""
Calculadora com while modelo 2
"""

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um operador: (+ - / *)')

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
        
    except ValueError as error:
        numeros_validos = False
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+ - / *'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador == '+':
        print(f'O resultado entre {num_1_float} + {num_2_float} é:', num_1_float + num_2_float)
    elif operador == '-':
        print(f'O resultado entre {num_1_float} - {num_2_float} é:', num_1_float - num_2_float)
    elif operador == '/':
        if num_2_float == 0:
            print('Não é possível dividir por zero.')
        else:
            print(f'O resultado entre {num_1_float} / {num_2_float} é:', num_1_float / num_2_float)
    elif operador == '*':
        print(f'O resultado entre {num_1_float} * {num_2_float} é:', num_1_float * num_2_float)
    else:
        print('Não foi possível calcular.')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
   
    if sair is True:
        break
