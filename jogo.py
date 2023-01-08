print('********************************')
print('Bem-vindo, ao jogo de advinhação')
print('********************************')

numero_secreto = 42
chute = int(input("Digite um numero: "))

if(numero_secreto == chute):
    print("Você digitou", chute, ", Você acertou!!!")
else:
    if(chute > numero_secreto):
        print('Você errou! Seu chute foi acima do número secreto')
    else:
        print('Você errou seu chute foi abaixo do número secreto')
print('Fim do jogo!')
