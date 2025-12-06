# NAME: Dominic Walters


from Game_Engine_Class import Game_engine
from Deck_Class import Deck

from random import shuffle
import time

#DEMO MATCH

#Creating the game and 2 decks of cards
gm = Game_engine()
plyr_deck = Deck()
opp_deck = Deck()

plyr_deck.create_deck()
opp_deck.create_deck()
gm.setup_game()

#Shuffling both decks
shuffle(plyr_deck.cards)
shuffle(opp_deck.cards)

#drawing a hands    
gm.draw_card(plyr_deck.cards_in_hand, plyr_deck.cards)
gm.draw_card(plyr_deck.cards_in_hand, plyr_deck.cards)
gm.draw_card(plyr_deck.cards_in_hand, plyr_deck.cards)
gm.draw_card(plyr_deck.cards_in_hand, plyr_deck.cards)
gm.draw_card(plyr_deck.cards_in_hand, plyr_deck.cards)

gm.draw_card(opp_deck.cards_in_hand, opp_deck.cards)
gm.draw_card(opp_deck.cards_in_hand, opp_deck.cards)
gm.draw_card(opp_deck.cards_in_hand, opp_deck.cards)
gm.draw_card(opp_deck.cards_in_hand, opp_deck.cards)
gm.draw_card(opp_deck.cards_in_hand, opp_deck.cards)


p_turn_counter = 1
o_turn_counter = 1
while gm.new_plyr.lp > 0 and gm.new_opp.lp > 0:
    #Player's Turn
    print(f"\n\n\n{gm.new_plyr.name}, Turn {p_turn_counter}: \n")
    gm.updating_the_board(plyr_deck, opp_deck, gm.new_plyr, gm.new_opp)
    print(gm.board)
    
        #draw card
    gm.draw_card(plyr_deck.cards_in_hand, plyr_deck.cards)
    gm.updating_the_board(plyr_deck, opp_deck, gm.new_plyr, gm.new_opp)
    print(gm.board)
    
        #play resources
    gm.play_resources(plyr_deck.cards_in_hand, plyr_deck.resources_in_play)
    gm.updating_the_board(plyr_deck, opp_deck, gm.new_plyr, gm.new_opp)
    print(gm.board)
    
        #play creatures
    gm.play_creature(plyr_deck.cards_in_hand, plyr_deck.battlefield,\
                        plyr_deck.resources_in_play, plyr_deck.discard_pile)
    gm.updating_the_board(plyr_deck, opp_deck, gm.new_plyr, gm.new_opp)
    print(gm.board)
    
        #attacking
    gm.attacking(plyr_deck.battlefield, gm.new_opp)
    gm.updating_the_board(plyr_deck, opp_deck, gm.new_plyr, gm.new_opp)
    print(gm.board)
    
        #ending turn
    gm.end_turn(plyr_deck, opp_deck)
    gm.updating_the_board(plyr_deck, opp_deck, gm.new_plyr, gm.new_opp)
    
    p_turn_counter += 1 #incrementing the player's turn
  
    if gm.new_opp.lp <= 0:
        break

    #Opponent's Turn
    print(f"\n\n\n{gm.new_opp.name}, Turn {o_turn_counter}: \n")
    gm.updating_the_board(plyr_deck, opp_deck, gm.new_plyr, gm.new_opp)
    print(gm.board)
    
        #draw card
    gm.draw_card(opp_deck.cards_in_hand, opp_deck.cards)
    gm.updating_the_board(plyr_deck, opp_deck, gm.new_plyr, gm.new_opp)
    print(gm.board)
    
        #play resources
    gm.play_resources(opp_deck.cards_in_hand, opp_deck.resources_in_play)
    gm.updating_the_board(plyr_deck, opp_deck, gm.new_plyr, gm.new_opp)
    print(gm.board)
    
        #play creatures
    gm.play_creature(opp_deck.cards_in_hand, opp_deck.battlefield,\
                        opp_deck.resources_in_play, opp_deck.discard_pile)
    gm.updating_the_board(plyr_deck, opp_deck, gm.new_plyr, gm.new_opp)
    print(gm.board)
    
        #attacking
    gm.attacking(opp_deck.battlefield, gm.new_plyr)
    gm.updating_the_board(plyr_deck, opp_deck, gm.new_plyr, gm.new_opp)
    print(gm.board)
    
        #ending turn
    gm.end_turn(plyr_deck, opp_deck)
    gm.updating_the_board(plyr_deck, opp_deck, gm.new_plyr, gm.new_opp)
    
    o_turn_counter += 1 #incrementing the opponent's turn

