import os

palavra_secreta = 'Macaco'.upper()
letras_corretas = ''
tentativas = 0

while True:
    os.system('cls')  # Limpa a tela
    print('Palavra formada: ', end='')

    # Mostra a palavra com as letras já acertadas e os asteriscos
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_corretas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(palavra_formada)

    # Se a palavra já estiver completa, o jogador vence
    if palavra_formada == palavra_secreta:
        print('Você ganhou! Parabéns!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', tentativas)
        jogar_novamente = input('Deseja jogar novamente? (s/n): ').strip().lower()
        if jogar_novamente != 's':
            break
        else:
            # Reiniciar o jogo
            palavra_secreta = 'Macaco'.upper()
            letras_corretas = ''
            tentativas = 0
            continue

    letra_digitada = input('Digite uma letra: ').upper()

    # Verifica se o usuário digitou mais de uma letra
    if len(letra_digitada) != 1:
        print('Digite apenas uma letra.')
        input('Pressione Enter para continuar...')
        continue

    # Verifica se a letra já foi digitada
    if letra_digitada in letras_corretas:
        print(f'Você já digitou a letra "{letra_digitada}".')
        input('Pressione Enter para continuar...')
        continue

    tentativas += 1

    # Se a letra estiver na palavra secreta, adiciona à lista de letras corretas
    if letra_digitada in palavra_secreta:
        letras_corretas += letra_digitada
    else:
        print(f'A letra "{letra_digitada}" não está na palavra.')
        input('Pressione Enter para continuar...')
