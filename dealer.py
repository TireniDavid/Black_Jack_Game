# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards. 
from random import randint
from end_status import blackjack_or_bust
from value import card_value
from name import draw
def play_dealer_turn():
  card_rank = randint(1,13)
  second_card_rank = randint(1,13)
  print (draw(card_rank))
  print (draw(second_card_rank))
  hand = card_value(card_rank) + card_value(second_card_rank)
  while hand < 17:
    print (f'Dealer has {hand}.')
    third_card_rank = randint(1,13)
    print(draw(third_card_rank))
    hand +=card_value(third_card_rank)
  print(f'Final hand: {hand}.')
  
  bj_or_bust = blackjack_or_bust(hand)
  if hand == 21:
    print(bj_or_bust)
    return bj_or_bust
  elif hand > 21 and hand <= 31:
    print(bj_or_bust)
    return bj_or_bust
  return None

  





