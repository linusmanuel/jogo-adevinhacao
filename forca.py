def jogar():
    print('********************************')
    print('Bem-vindo, ao jogo de Forca')
    print('********************************')

    palavra_secreta = 'banana'
    acertou = False
    enforcou = False
    index = 0

    while(not enforcou and not acertou):
        chute = input('Qual letra: ').strip()
        for letra in palavra_secreta:
            if(letra.upper() == chute.upper()):
                index += 1
                print(f'Encontrei a letra {letra} na posição {index}')

    print('Fim do jogo!')

if(__name__ == '__main__'):
    jogar()