import adivinhacao
import Forca


def escolhe_jogo():
    print("*" * 50)
    print("Escolha o seu jogo!")
    print("*" * 50)

    print(' (1) - Forca\n (2) - Adivinhação')
    escolha_usuario = int(input('Escolha o jogo: '))
    if escolha_usuario == 1:
        print('Jogo da Forca começando!')
        Forca.jogar()
    elif escolha_usuario == 2:
        print('Jogo da adivinhação começando!')
        adivinhacao.jogar()


if __name__ == "__main__":
    escolhe_jogo()


