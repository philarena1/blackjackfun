# file for each hand played

class Game():

    def __init__(self):
        # default game 1 player, 6 decks
        Game.players = 5
        Game.decks = 6
        Game.deck_cards = [] # list of actual cards available
        Game.shuffle_rate = 6 #times deck is shuffled
        Game.people_at_table = []


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



    def start_game(self):
        #deal out inital cards
        people_at_table = self.players
        people = list(range(1, people_at_table + 1))

        list_people = []
        for i in people:
            person_name = 'person_%s' %(str(i))

            person = Person()
            person.name = person_name
            list_people.append(person)

        print(list_people)
        self.people_at_table = list_people

    def simulate(self, n):
        """ n is the number of simulations to run"""



class Person():
    # people at table

    def __init__(self):
        self.name = ''
        self.first_card = ''
        self.second_card = ''
        self.hit_cards = ''
        self.split = ''
        self.split2 = ''
        self.split3 = ''
        self.stay = False




class Hand():

    def __init__(self):
        Hand.cards_drawn = 0
        Hand.splits = 0
        Hand.bet = 0
        Hand.cards_list_drawn = []  # list of cards drawn in the same hand

    def hit(self, game_deck):
        # pull a card
        # pop card from deck, store in results
        hit_card = game_deck.pop()
        self.cards_list_drawn.append(hit_card)
        self.cards_drawn = self.cards_drawn + 1
        print('hit %s' % str(hit_card))
        print(hit_card)

    def stay(self):
        # stay
        self.stay = True
        print('stay')

    def double(self):
        #increase wager
        print('double')

    def split(self):
        #Pull extra card
        print('split')


new_game = Game()
new_game.get_fresh_deck()
new_game.start_game()
new_game.people_at_table[0].name

hand = Hand()

hand.hit(new_game.deck_cards)

