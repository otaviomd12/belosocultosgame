# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Ray")
define b = Character("Math")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene cenario 1 

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    show menina

    e "Eu nao quero falar nada."

    e "Acabou o jogo.FIM>"

    hide menina

    # This ends the game.
    with fade
    scene cenario 2

    show menina at right
    show menino imagem

    # These display lines of dialogue.

    b "Ja deu cara, VAI EMBORA"

    # This ends the game.

    # raxitegui aqui comeca o jogo

    b "Voce ainda vai continuar aqui?"

menu:

    "Continuar insistindo em jogar.":
        jump choco1

    "Terminar o jogo.":
        jump choco2

label choco1:

    b "Cara ja que voce nao vai embora, nos vamos!."

    jump menina

label choco2:

    b "Que bom que voce entendeu que nao existe um jogo aqui."

    jump menina

label menina:

    hide menina
    hide menino imagem

    ".:. Fim de Jogo."

    return
