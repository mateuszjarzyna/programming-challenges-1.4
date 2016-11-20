import random

class NumberGame() :
    def __init__(self):
        self.new_game()

    def new_game(self):
        self.number = random.randint(0, 100)
        self.won = False
        #print("I m thing about ", self.number)

    def guess(self, x):
        if self.won is True:
            print("You have already won")
            return

        if x > self.number:
            print("Too high")
        elif x < self.number:
            print("Too low")
        else:
            self.won = True
            print("You won!")
