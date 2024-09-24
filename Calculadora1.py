"""
Calculadora com while modelo 1
"""

def input_int_or_float(prompt):
    while True:
        user_input = input(prompt)
        try:
            # tenta converter para inteiro
            return int(user_input)
        except ValueError:
            try:
                # se falhar, tenta converter para float
                return float(user_input)
            except ValueError:
                # se nenhum dos dois funcionar, pede novamente
                print('Por favor, insira um número válido')

def input_operador():
    while True:
        operador = input('Digite o operador (+, -, *, /): ')
        if operador in ['+', '-', '*', '/']:  # Corrigido o erro de sintaxe
            return operador
        else:
            print('Operador inválido. Por favor, escolha entre +, -, * ou /')

# Exemplo de uso

primeiro_numero = input_int_or_float('Digite o primeiro número: ')
segundo_numero = input_int_or_float('Digite o segundo número: ')
operador = input_operador()  # Corrigido o erro na chamada da função

# Aplicando o operador lógico
if operador == '+':
    resultado = primeiro_numero + segundo_numero
elif operador == '-':
    resultado = primeiro_numero - segundo_numero
elif operador == '*':
    resultado = primeiro_numero * segundo_numero
elif operador == '/':
    if segundo_numero != 0:
        resultado = primeiro_numero / segundo_numero
    else:
        resultado = "Erro: Divisão por zero!"

print(f'O resultado de {primeiro_numero} {operador} {segundo_numero} é: {resultado}')

