# file for each hand played

class Game():

    def __init__(self):
        # default game 1 player, 6 decks
        Game.players = 2
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

        dealer = Person()
        dealer.name = 'DEALER'
        list_people.append(dealer)

        print(list_people)
        self.people_at_table = list_people


    def deal(self):
        # deal cards for each person
        for person in self.people_at_table:
            new_card = self.deck_cards.pop()
            newHand = Hand()
            hand_id = person.name + str(int(time.time())) # generate unique id for each hand
            newHand.id = hand_id
            new_card_list = [new_card]
            newHand.cards_list_drawn = (new_card_list)
            person.person_hands.append(newHand)



    def simulate(self, n):
        """ n is the number of simulations to run"""



class Person():
    # people at table

    def __init__(self):
        self.name = ''
        self.person_hands = [] # list of hands played





class Hand():

    def __init__(self):
        Hand.id = ''
        Hand.cards_drawn = 0
        Hand.splits = 0 # if is a split, and Ace, only 1 card
        Hand.bet = 1
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
        double = self.bet * 2
        self.bet = double

        print('double')
        print('new bet %s' % str(double))

    def split(self):
        #Pull extra card
        # create 1 sub hand
        self.splits = 1

        split_hand = Hand()
        split_hand.splits = 1
        print('split')



# 1 game example
newGame = Game()
newGame.start_game()
newGame.get_fresh_deck()
newGame.deal()

# see players hands
newGame.people_at_table[0].person_hands[0].cards_list_drawn
for people in newGame.people_at_table:
    print(people.name)
    print(people.person_hands[0].cards_list_drawn)

