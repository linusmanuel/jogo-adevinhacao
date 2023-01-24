from random import randrange
print('********************************')
print('Bem-vindo, ao jogo de advinhação')
print('********************************')

numero_secreto = randrange(1, 101)
total_de_tentativas = 3

for rodada in range(0, total_de_tentativas):
    print(f'TENTATIVA  {rodada}  de {total_de_tentativas}')
    print(f'Numero secreto: {numero_secreto}')
    chute = int(input("Digite um numero: "))

    if(chute < 0 or chute > 100):
        print('Número inválido, digite um número entre 1 e 100!')
        continue

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto


    if(acertou):
        print("Você digitou", chute, ", Você acertou!!!")
        break
    elif(maior):
        print('Você errou! Seu chute foi acima do número secreto')
    elif(menor):
        print('Você errou seu chute foi abaixo do número secreto')
    rodada += 1
print('Fim do jogo!')
