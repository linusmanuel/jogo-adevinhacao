def jogar():
    print('********************************')
    print('Bem-vindo, ao jogo de Forca')
    print('********************************')

    palavra_secreta = 'banana'
    letras_acertadas = ['_','_','_','_','_','_']

    acertou = False
    enforcou = False

    while(not enforcou and not acertou):
        chute = input('Qual letra: ').strip()

        index = 0
        for letra in palavra_secreta:
            if(letra.lower() == chute.lower()):
                letras_acertadas[index] = letra
            index += 1
        print(letras_acertadas)


if(__name__ == '__main__'):
    jogar()

# Em desenvolvimento { Dá um desconto no código LOL :) }
