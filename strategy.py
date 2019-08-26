def get_numb(card):
    card = card.replace('H','')
    card = card.replace('S', '')
    card = card.replace('C', '')
    card = card.replace('D', '')

    if card in ['J','Q','K']:
        card = 10

    if card == 'A':
        card = 11

    return card

def what_to_do(card1,card2,deal):
    ### what to do
    # 1) see if we can split
    #card1 = get_numb(card1)
    #card2 = get_numb(card2)
    hand_sum = int(card1) + int(card2)

    if hand_sum >= 4 and hand_sum <= 8:
        action = 'hit'

    if hand_sum == 9 and deal == 2:
        action = ('hit')

    if hand_sum == 9 and deal >= 3 and deal <= 6:
        action = ('double down')

    if hand_sum == 9 and deal >= 7 and deal <= 11:
        action = ('double down')

    if hand_sum == 10 and deal >= 2 and deal <= 9:
        action = ('double down')

    if hand_sum == 10 and deal >= 10 and deal <= 11:
        action = ('hit')

    if hand_sum == 11:
        action = ('double down')

    if hand_sum == 12 and deal >= 2 and deal <= 3:
        action = ('hit')

    if hand_sum == 12 and deal >= 4 and deal <= 6:
        action = ('stay')

    if hand_sum == 12 and deal >= 7 and deal <= 11:
        action = ('hit')

    if hand_sum >= 13 and hand_sum <= 16 and deal >= 2 and deal <= 6:
        action = ('stay')

    if hand_sum >= 13 and hand_sum <= 16 and deal >= 7 and deal <= 11:
        action = ('hit')

    if hand_sum >= 17 and hand_sum <= 21:
        action = ('stay')

    print("you have %s against the dealer's %s" % (hand_sum, deal))

    return action


