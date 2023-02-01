from random import randrange
def jogar():
    print('********************************')
    print('Bem-vindo, ao jogo de advinhação')
    print('********************************')

    numero_secreto = randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print('Qual o nível de diuficildade?')
    print('(1) Fácil (2) Médio (3) Díficil')

    nivel = int(input('Define o nível: '))

    if(nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(0, total_de_tentativas):
        print(f'TENTATIVA  {rodada}  de {total_de_tentativas}')
        chute = int(input("Digite um numero: "))

        if(chute < 0 or chute > 100):
            print('Número inválido, digite um número entre 1 e 100!')
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto


        if(acertou):
            print(f"Você acertou e fez {pontos} pontos!")
            break
        else:
            if(maior):
                print('Você errou! Seu chute foi acima do número secreto')
            elif(menor):
                print('Você errou seu chute foi abaixo do número secreto')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos
        rodada += 1
    print('Fim do jogo!')

if(__name__ == '__main__'):
    jogar()
