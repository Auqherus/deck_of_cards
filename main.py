import random


class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self):
        self.__cards = []
        self.create_deck()

    def create_deck(self):
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.__cards.append((rank, suit))

    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def deal_card(self):
        try:
           return self.__cards.pop()
        except IndexError:
            return None
        
    def get_deck_info(self):
        return self.__cards
            

    # don't touch below this line

    def __str__(self):
        return f"The deck has {len(self.__cards)} cards"
    
def main(): # for some testing

    deck1 = DeckOfCards()
    deck1.shuffle_deck()

    for card in deck1.get_deck_info():
        print(card)

main()
