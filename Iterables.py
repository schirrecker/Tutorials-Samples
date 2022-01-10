#for byte in b'Binary':
#    print(byte)

'''
c = 213749124918345
digits = [int(d) for d in str(c)]

for digit in digits:
    print(digit)
'''

usernames = ('Rainer', "Alfons", 'John')

'''
looper1 = usernames.__iter__()
print(type(looper1))
print(looper1.__next__())
print(looper1.__next__())
print(looper1.__next__())
print(looper1.__next__())
'''

'''
looper2 = iter(usernames)
print(next(looper2))
print(next(looper2))
print(next(looper2))
print(next(looper2))
'''

'''
users = ['moi', 'toi', 'elle', 'lui']
# for user in users:
#    print(user)

looper = iter(users)
while True:
    try:
        user = next(looper)
        print(user)
    except StopIteration:
        break
'''

'''
class Portfolio:
    def __init__(self):
        self.holdings = {}

    def buy(self, stock, nb_shares):
        self.holdings[stock] = self.holdings.get(stock, 0) + nb_shares  # default value is 0 shares

    def sell(self, stock, nb_shares):
        self.holdings[stock] = self.holdings.get(stock, 0) - nb_shares

    def __iter__(self):
        return iter(self.holdings.items())

p = Portfolio()

p.buy("ALPHA", 5)
p.buy("BETA", 10)
p.buy("BETA", 17)
p.buy("GAMMA", 23)
p.sell("BETA", 5)

for (stock, nb_shares) in p:
    print (stock, nb_shares)
'''

import itertools
ranks = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
ranks = [str(rank) for rank in ranks]
# print(ranks)
suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

deck = [card for card in itertools.product(ranks, suits)]

#for (index, card) in enumerate(deck):
#    print(1 + index, card)

hands = [hand for hand in itertools.combinations(deck, 5)]
print(f"The number of hands is {len(hands)}.")
