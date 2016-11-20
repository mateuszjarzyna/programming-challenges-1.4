from number_game import NumberGame

def play():
    game = NumberGame()
    while (game.won is False):
        choosen = int(input('Choose a number: '))
        game.guess(choosen)

if __name__ == '__main__':
    print("Let's play a game")
    print("Guess number I'm thing about")

    while (True):
        play()
        answer = input("Wanna play again? [Yes/No] ")
        if answer != "Yes":
            break
