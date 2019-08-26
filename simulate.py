from hand import *
from strategy import *

# 1 game example
newGame = Game()

newGame.deal()

# see players hands
newGame.people_at_table[0].person_hands[0].cards_list_drawn
for people in newGame.people_at_table:
    print(people.name)
    print(people.person_hands[0].cards_list_drawn)

newGame.people_at_table[0].person_hands[0].cards_list_drawn

# test hit
newGame.people_at_table[0].person_hands[0].cards_list_drawn
newGame.people_at_table[0].person_hands[0].hit(newGame.deck_cards)
newGame.people_at_table[0].person_hands[0].cards_list_drawn

# stay hit
newGame.people_at_table[0].person_hands[0].stay()




# get dealer's hand
dealer_show = 'None'
for people in newGame.people_at_table:
    if (people.name) == 'DEALER':
        dealer_show = (people.person_hands[0].cards_list_drawn[0]) # first card

action = 'unknown'
for people in newGame.people_at_table:
    if (people.name) != 'DEALER':
        first_card, second_card = people.person_hands[0].cards_list_drawn[0],people.person_hands[0].cards_list_drawn[1]  # first card
        first_card = get_numb(first_card)
        second_card = get_numb(second_card)
        print(first_card)
        print(second_card)
        action = what_to_do(first_card, second_card, dealer_show)
        print(action)