import random
import math

class GuessingGame:
    MAX_GUESSES = 7
    
    def __init__(self, min_num, max_num):
        self.min = min_num
        self.max = max_num
        self.reset()
    
    def reset(self):
        self.guesses = int(math.log2(self.max - self.min + 1)) + 1
        self.number = random.randint(self.min, self.max)
 
    def print_guesses(self):
        if self.guesses == 1:
            print("You have 1 guess remaining.")
        else:
            print(f"You have {self.guesses} guesses remaining.")
    
    def get_guess(self):
        while True:
            user_input = input(
                f"Enter a number between {self.min} and {self.max}: "
            )

            if user_input.isdigit():
                guess = int(user_input)

                if self.min <= guess <= self.max:
                    return guess

            print("Invalid guess.")
        
    def play(self):
        self.reset()
        won = False
        print()
        
        while self.guesses and not won:
            self.print_guesses()
            guess = self.get_guess()
            self.guesses -= 1
            
            if guess < self.number:
                print("Your guess is too low.")
            elif guess > self.number:
                print("Your guess is too high.")
            else:
                print("That's the number!")
                won = True
        
            print()
            
        if won:
            print("You won!")
        else:
            print("You have no more guesses. You lost!")
            
        print()
        
game = GuessingGame(501, 1500)
game.play()

