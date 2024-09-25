palavra_secreta = 'Macaco'
tentativa_usuario = ''
letras_corretas = ['_' for letra in palavra_secreta] # Exibe letras adivinhas ou espaços
tentativas = 0
tentativas_maximas = 20 # limite max de tentativas


while ''.join(letras_corretas) != palavra_secreta and tentativas < tentativas_maximas:
    print('Palavra:', ' '.join(letras_corretas))
    letra = input(f'Tentativa {tentativas + 1} - Informe uma letra: ').strip().upper()
    tentativas += 1

    if letra in palavra_secreta.upper():
        for i, letra_secreta in enumerate(palavra_secreta.upper()):
            if letra_secreta == letra:
                letras_corretas[i] = palavra_secreta[i] # revela a letra correta
    else:
        print(f'A letra {letra} não está na palavra.')

if ''.join(letras_corretas) == palavra_secreta:
    print(f'Parabéns! Você adivinhou a palavra secreta: {palavra_secreta} em {tentativas} tentativas.')
else:
    print(f'Você perdeu! A palavra secreta era {palavra_secreta}')
