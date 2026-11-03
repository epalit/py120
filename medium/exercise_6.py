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
    
    def __init__(self, num_cards=52):
        self.new_deck(num_cards)
        
    def new_deck(self, num_cards=52):
        self.cards = [
            Card(rank, suit)
            for suit in Deck.SUITS
            for rank in Deck.RANKS
        ]
        if num_cards < 52:
            self.cards = random.choices(self.cards, k=num_cards)
        self.shuffle()
    
    def draw(self):
        if not self.cards:
            self.new_deck()
    
        return self.cards.pop()
    
    def shuffle(self):
        random.shuffle(self.cards)

    def get_suits(self):
        return [card.suit for card in self.cards]

    def get_ranks(self):
        return [card.rank for card in self.cards]

    def _get_values(self):
        return [card.get_value() for card in self.cards]

    def is_single_suit(self):
        return len(set(self.get_suits())) == 1

    def get_rank_counts(self):
        counts = {}
        for rank in self.get_ranks():
            counts[rank] = counts.get(rank, 0) + 1

        return list(counts.values())

    def is_consecutive(self):
        values = self._get_values()
        values.sort()

        return values[4] - values[3] == 1 and \
        values[3] - values[2] == 1 and \
        values[2] - values[1] == 1 and \
        values[1] - values[0] == 1

class PokerHand:
    ROYAL_RANKS = ['Jack', 'Queen', 'King', 'Ace', 10]

    def __init__(self, deck):
        self.deck = deck

    def print(self):
        for card in self.deck.cards:
            print(card)

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"

    def _is_royal_flush(self):
        return self.deck.is_single_suit() and \
            set(self.deck.get_ranks()) == set(PokerHand.ROYAL_RANKS)

    def _is_straight_flush(self):
        return self.deck.is_consecutive() and self.deck.is_single_suit()

    def _is_four_of_a_kind(self):
        return 4 in self.deck.get_rank_counts()

    def _is_full_house(self):
        rank_count_values = self.deck.get_rank_counts()
        return 3 in rank_count_values and 2 in rank_count_values

    def _is_flush(self):
        return self.deck.is_single_suit()

    def _is_straight(self):
        return self.deck.is_consecutive()

    def _is_three_of_a_kind(self):
        return 3 in self.deck.get_rank_counts()

    def _is_two_pair(self):
        rank_count_values = self.deck.get_rank_counts()
        return rank_count_values.count(2) == 2

    def _is_pair(self):
        return 2 in self.deck.get_rank_counts()

hand = PokerHand(Deck(5))
hand.print()
print(hand.evaluate())
print()

# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self.cards = cards

# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print("Royal Flush: ", hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print("Straight Flush: ", hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print("Four of a kind: ", hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print("Full house: ", hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print("Flush: ", hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print("Straight: ", hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print("Straight: ", hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print("Three of a kind: ", hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print("Two pair: ", hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print("Pair: ", hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print("High card: ", hand.evaluate() == "High card")
