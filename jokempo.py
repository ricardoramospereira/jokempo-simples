import random

from img import pedra, papel, tesoura


img_game = [pedra, papel, tesoura]

pc = random.randint(0, 2)
user = int(input('Escolha sua opção:\n [0] Pedra\n [1] Papel\n [2] Tesoura\n'))

print('Jogador')
print(img_game[user])
print('Pc')
print(img_game[pc])


if user == 0 and pc == 0:
    print('Empate')
elif user == 0 and pc == 1:
    print('Você perdeu')
elif user == 0 and pc == 2:
    print('Você ganhou')
elif user == 1 and pc == 0:
    print('Você ganhou')
elif user == 1 and pc == 1:
    print('Empate')
elif user == 1 and pc == 2:
    print('Você perdeu')
elif user == 2 and pc == 0:
    print('Você perdeu')
elif user == 2 and pc == 1:
    print('Você ganhou')
elif user == 2 and pc == 2:
    print('Empate')
