from time import sleep
from random import randint


def jogar():

    print("*" * 50)
    print("Jogo da adivinhação!")
    print("*" * 50)
    numero_pc = randint(0, 10)
    tentativas_usuario = 0
    pontos_usuario = 1000
    sleep(2)
    print('Vamos começar o jogo.')
    sleep(1)
    print('Primeiramente, escolha a dificuldade:')
    print('(1) - Fácil \n (2) - Médio \n (3) - Difícil')

    nivel_jogo = int(input('Defina o nível: '))

    if nivel_jogo == 1:
        tentativas_usuario = 20
    elif nivel_jogo == 2:
        tentativas_usuario = 5
    else:
        tentativas_usuario = 3

    print('Agora vamos lá! Eu pensei em um número de 1 à 10, tente adivinhar.')
    for rodada in range(1, tentativas_usuario + 1):
        print(f'Tentativa {rodada} de {tentativas_usuario}')
        chute_usuario = int(input("Eu pensei no número: "))

        if chute_usuario < 1 or chute_usuario > 10:
            print('Escolha um número entre 1 e 10 apenas.')
            continue
        if chute_usuario == numero_pc:
            print(f'Parabéns, você acertou e fez {pontos_usuario} pontos')
            break
        if chute_usuario < numero_pc:
            print('Seu número foi abaixo do escolhido')
        else:
            print('Seu número foi acima do escolhido')
        pontos_perdidos = abs(numero_pc - chute_usuario)
        pontos_usuario = pontos_usuario - pontos_perdidos
    if chute_usuario == numero_pc:
        print(f'Fim de jogo, você ganhou! O número escolhido foi {numero_pc}')
    else:
        print(f'Fim do jogo, você perdeu! O número escolhido foi {numero_pc}')


if __name__ == "__main__":
    jogar()
