print('********************************')
print('Bem-vindo, ao jogo de advinhação')
print('********************************')

numero_secreto = 42
chute = int(input("Digite um numero: "))

acertou = numero_secreto == chute
maior = chute > numero_secreto
menor = chute < numero_secreto

if(acertou):
    print("Você digitou", chute, ", Você acertou!!!")
elif(maior):
    print('Você errou! Seu chute foi acima do número secreto')
elif(menor):
    print('Você errou seu chute foi abaixo do número secreto')
print('Fim do jogo!')
