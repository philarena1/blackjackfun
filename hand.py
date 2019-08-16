# file for each hand played

class Game():

    def __init__(self):
        # default game 1 player, 6 decks
        Game.players = 1
        Game.decks = 6
        Game.deck_cards = [] # list of actual cards available
        Game.shuffle_rate = 6 #times deck is shuffled



    def test(self):
        print('test')


    def get_fresh_deck(self):
        suits = ['H', 'S', 'C', 'D']
        numbs = list(range(2, 11))

        faces = ['J', 'Q', 'K', 'A']

        deck = numbs + faces

        full_deck = []
        for suit in suits:
            for card in deck:
                full_deck.append(str(card) + suit)

        num_decks = self.decks
        total_decks = full_deck * num_decks

        # dealer rules, hits on
        from random import shuffle
        shuffle_num = self.shuffle_rate  # how many times to shuffle

        i = 0
        while i < shuffle_num:
            shuffle(total_decks)
            i = i + 1

        self.deck_cards = total_decks



    def simulate(self, n):
        """ n is the number of simulations to run"""




class Hand():

    def __init__(self):
        Hand.cards_drawn = 0
        Hand.splits = 0
        Hand.bet = 0

    def hit(self):
        # pull a card
        print('hit')

    def stay(self):
        # stay
        print('stay')

    def double(self):
        #increase wager
        print('double')

    def split(self):
        #Pull extra card
        print('split')


new_game = Game()
new_game.get_fresh_deck()


hand = Hand()



