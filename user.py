# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards. 
from random import randint
from end_status import blackjack_or_bust
from value import card_value
from name import draw
# Write all of your part 2B code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
def play_human_turn():
  card_rank = randint(1,13)
  second_card_rank = randint(1,13)
  print(draw(card_rank))
  print(draw(second_card_rank))
  hand = card_value(card_rank) + card_value(second_card_rank)
  while hand < 21:
    prompt=input("You have " + str(hand) + ". Hit (y/n)? " )
    if prompt == 'y':
      third_card_rank = randint(1,13)
      print(draw(third_card_rank))
      hand += card_value(third_card_rank)
    elif prompt == 'n':
      print("Final hand: " + str(hand) + ".")
      break
    else:
      print("Sorry I didn't get that.")
   

  if hand == 21:
    print("Final hand: " + str(hand) + ".") 
    print( blackjack_or_bust(hand))
    return blackjack_or_bust(hand)
    
  elif hand > 21:
    print("Final hand: " + str(hand) + ".")
    print( blackjack_or_bust(hand))
    return blackjack_or_bust(hand)
    
