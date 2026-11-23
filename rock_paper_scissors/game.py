import random

class Player:
    CHOICES = ('rock', 'paper', 'scissors')

    def __init__(self, player_type):
        self._player_type = player_type.lower()
        self.move = None

    def _is_human(self):
        return self._player_type == 'human'

    def choose(self):
        if self._is_human():
            prompt = 'Please choose rock, paper, or scissors: '

            while True:
                choice = input(prompt).lower()
                if choice in Player.CHOICES:
                    break

                print(f'Sorry, {choice} is not valid')

            self.move = choice
        else:
            self.move = random.choice(Player.CHOICES)

class Move:
    def __init__(self):
        pass

class Rule:
    def __init__(self):
        pass

    def compare(self, move1, move2):
        pass

class RPSGame:
    def __init__(self):
        self._human = Player('human')
        self._computer = Player('computer')

    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors!')

    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')

    def _display_winner(self):
        human_move = self._human.move
        computer_move = self._computer.move

        print(f'You chose: {human_move}')
        print(f'The computer chose: {computer_move}')

        if ((human_move == 'rock' and computer_move == 'scissors') or
            (human_move == 'paper' and computer_move == 'rock') or
            (human_move == 'scissors' and computer_move == 'paper')):

            print('You win!')
        elif ((computer_move == 'rock' and human_move == 'scissors') or
              (computer_move == 'paper' and human_move == 'rock') or
              (computer_move == 'scissors' and human_move == 'paper')):

            print('Computer wins!')
        else:
            print("It's a tie")

    def _play_again(self):
        answer = input('Would you like to play again? (y/n) ')
        return answer.lower().startswith('y')

    def play(self):
        self._display_welcome_message()

        while True:
            self._human.choose()
            self._computer.choose()
            self._display_winner()
            if not self._play_again():
                break

        self._display_goodbye_message()

RPSGame().play()