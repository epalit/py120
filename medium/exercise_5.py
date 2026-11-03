import random
class Card:
    CARD_VALUES = {
        'Ace': 14,
        'King': 13,
        'Queen': 12,
        'Jack': 11,
    }
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def get_value(self):
        return Card.CARD_VALUES.get(self.rank, self.rank)
    
    def __gt__(self, other):
        return self.get_value() > other.get_value()
    
    def __lt__(self, other):
        return self.get_value() < other.get_value()
    
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    
    def __init__(self):
        self.new_deck()
        
    def new_deck(self):
        self.cards = [
            Card(rank, suit)
            for suit in Deck.SUITS
            for rank in Deck.RANKS
        ]
        self.shuffle()
    
    def draw(self):
        if not self.cards:
            self.new_deck()
    
        return self.cards.pop()
    
    def shuffle(self):
        random.shuffle(self.cards)

deck = Deck()
drawn = []
for _ in range(52):
    drawn.append(deck.draw())

count_rank_5 = sum([1 for card in drawn if card.rank == 5])
count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

print(count_rank_5 == 4)      # True
print(count_hearts == 13)     # True

drawn2 = []
for _ in range(52):
    drawn2.append(deck.draw())

print(drawn != drawn2)        # True (Almost always).

