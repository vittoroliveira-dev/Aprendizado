cpf = '13682791205'
nove_digitos = cpf[:9]

# Cálculo do primeiro dígito verificador
contador_regressivo_1 = 10
resultado_1 = 0

for digito_1 in nove_digitos:
    resultado_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1

resto = resultado_1 % 11
primeiro_digito = 0 if resto < 2 else 11 - resto
print(primeiro_digito)

# Adiciona o primeiro dígito ao CPF para calcular o segundo dígito
dez_digitos = nove_digitos + str(primeiro_digito)

# Cálculo do segundo dígito verificador
contador_regressivo_2 = 11
resultado_2 = 0

for digito_2 in dez_digitos:
    resultado_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1

resto2 = resultado_2 % 11
segundo_digito = 0 if resto2 < 2 else 11 - resto2
print(segundo_digito)
