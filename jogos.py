import advinhacao
import forca
def escolhe_jogo():
    print('********************************')
    print('*****  Escolhe o seu Jogo  *****')
    print('********************************')

    print('(1) Forca, (2) Advinhacação')
    jogo = int(input('Qual jogo você quer? '))

    if (jogo == 1):
        forca.jogar()
    elif (jogo == 2):
        advinhacao.jogar()

if(__name__ == '__main__'):
    escolhe_jogo()