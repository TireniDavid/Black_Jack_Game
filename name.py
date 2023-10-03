def draw(card_rank):
    if card_rank == 1:
        card_name = "Ace"
    elif card_rank == 11:
        card_name = "Jack"
    elif card_rank == 12:
        card_name = "Queen"
    elif card_rank == 13:
        card_name = "King"
    elif card_rank < 1 or card_rank > 13:
        return 'BAD CARD'
    else:
        card_name = str(card_rank)
    if card_rank == 1 or card_rank == 8:
        drew_prefix = "Drew an "
    else:
        drew_prefix = "Drew a "
    return drew_prefix + card_name
#you can test it and see
