def jogar():
    print('********************************')
    print('Bem-vindo, ao jogo de Forca')
    print('********************************')
    print('Fim do jogo!')

    palavra_secreta = 'banana'
    acertou = False
    enforcou = False
    index = 0

    while(not enforcou and not acertou):
        chute = input('Qual letra: ')
        for letra in palavra_secreta:
            if(letra == chute):
                index += 1
                print(f'Encontrei a letra {letra} na posição {index}')

if(__name__ == '__main__'):
    jogar()