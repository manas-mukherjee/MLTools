import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()
print(len(deck))
print(deck.__getitem__(0))
print(deck[0])

beer_card = Card('7', 'diamonds')
print(beer_card)

#random choice
from random import choice
print("Random card : ", choice(deck))

#slicing
print(deck[:3])
print(deck[12::13])

#iterable
for card in deck:
    print(card)

#iterable - reversed
print('iterable reversed') # doctest: +ELLIPSIS
for card in reversed(deck):
    print(card)

#in operation
print(Card('Q', 'hearts') in deck)

#Sorting. Aces has highest value. spades (highest), then hearts, diamonds, and clubs (lowest)
#https://www.programiz.com/python-programming/methods/list/index
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    suit_value = suit_values[card.suit]
    return rank_value * len(suit_values) + suit_value

print('card ranks')
for card in sorted(deck, key=spades_high):
    print(card)
