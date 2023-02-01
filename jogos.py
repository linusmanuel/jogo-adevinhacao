import advinhacao
import forca

print('********************************')
print('*****  Escolhe o seu Jogo  *****')
print('********************************')

print('(1) Forca, (2) Advinhacação')
jogo = int(input('Qual jogo você quer? '))

if (jogo == 1):
    forca.jogar()
elif (jogo == 2):
    advinhacao.jogar()