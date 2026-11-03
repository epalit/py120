import random

class GuessingGame:
    MAX_GUESSES = 7
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.guesses = self.MAX_GUESSES
        self.number = random.randint(self.MIN_NUMBER, self.MAX_NUMBER)
 
    def print_guesses(self):
        if self.guesses == 1:
            print("You have 1 guess remaining.")
        else:
            print(f"You have {self.guesses} guesses remaining.")
    
    def get_guess(self):
        while True:
            user_input = input(
                f"Enter a number between {self.MIN_NUMBER} and {self.MAX_NUMBER}: "
            )

            if user_input.isdigit():
                guess = int(user_input)

                if self.MIN_NUMBER <= guess <= self.MAX_NUMBER:
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
        
game = GuessingGame()
game.play()

