print('********************************')
print('Bem-vindo, ao jogo de advinhação')
print('********************************')

numero_secreto = 42
chute = int(input("Digite um numero: "))

if(numero_secreto == chute):
    print("Você digitou", chute, ", Você acertou!!!")
else:
    print('Você errou!')
print('Fim do jogo!')
