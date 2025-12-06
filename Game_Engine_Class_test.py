# NAME: Dominic Walters


from unittest.mock import patch
from Creature_Class import Creature
from Resource_Class import Resource
from Game_Engine_Class import Game_engine
from Deck_Class import Deck
from random import shuffle

new_game = Game_engine()
# new_game.setup_game()
# setup_game() does the following:
    # getting_player_name()
    # explaining_rules()
    # starting_game()


new_game.__init__() #Testing the initial game setup

assert new_game.name == ""
assert new_game.new_plyr.name == ""
assert new_game.game_over == False
assert new_game.game_started == False
assert new_game.new_plyr.lp == 10
assert new_game.new_opp.lp == 10
assert new_game.winner == None


#testing getting_player_name()
with patch('builtins.input', return_value = "Dom"):
    expected_name = new_game.getting_player_name()

assert expected_name == "Dom"
assert new_game.new_plyr.name == "Dom"


new_game.__init__() #resetting variable data


#testing explaining_rules()
# with patch('builtins.input', return_value = "Y"):
#     expected_result = new_game.explaining_rules()
    
# assert expected_result == 


#testing staring_game()
    #testing with the input "Y"
new_game.starting_game()

assert new_game.game_started == True


new_game.__init__() #resetting variable data


#testing checking_for_gameover() and determining_the_winner()

    #instance where player_1 loses w/0 lp:
new_game.new_plyr.lp = 0
new_game.checking_for_gameover()
assert new_game.game_over == True
assert new_game.game_started == False
assert new_game.winner == False
       
new_game.__init__() #resetting values

    #instance where new_opp loses w/0 lp:
new_game.new_opp.lp = 0
new_game.checking_for_gameover()
assert new_game.game_over == True
assert new_game.game_started == False
assert new_game.winner == True
       
new_game.__init__() #resetting values

    #instance where player_1 loses w/less than 0 lp:
new_game.new_plyr.lp = -1
new_game.checking_for_gameover()
assert new_game.game_over == True
assert new_game.game_started == False
assert new_game.winner == False
        
new_game.__init__() #resetting values

    #instance where new_opp loses w/less than 0 lp:
new_game.new_opp.lp = -1
new_game.checking_for_gameover()
assert new_game.game_over == True
assert new_game.game_started == False
assert new_game.winner == True
        
new_game.__init__() #resetting values

    #instance where new_opp wins w/1 lp:
new_game.new_plyr.lp = 0
new_game.new_opp.lp = 1
new_game.checking_for_gameover()
assert new_game.game_over == True
assert new_game.game_started == False
assert new_game.winner == False
        
new_game.__init__() #resetting values

    #insstance where new_plyr wins w/1 lp:
new_game.new_opp.lp = 0
new_game.new_plyr.lp = 1
new_game.checking_for_gameover()
assert new_game.game_over == True
assert new_game.game_started == False
assert new_game.winner == True
        
new_game.__init__() #resetting values

    #instance where neither player wins:
new_game.new_plyr.lp = 0
new_game.new_opp.lp = 0
new_game.checking_for_gameover()
assert new_game.game_over == True
assert new_game.game_started == False
assert new_game.winner == None
        
new_game.__init__() #resetting values
        
new_game.game_started = True #setting the variable indicating a started game to true

    #instance where both players still alive:
new_game.new_plyr.lp = 1
new_game.new_opp.lp = 1
new_game.checking_for_gameover()
assert new_game.game_over == False
assert new_game.game_started == True
assert new_game.winner == None
        
new_game.__init__() #resetting values


#ASSIGNMENTS 2
    

plyr_test_deck = Deck()
opp_test_deck = Deck()
plyr_test_deck.create_deck()
opp_test_deck.create_deck()

    #testing draw_card():
assert len(plyr_test_deck.cards) == 20          #confirming the initial list length of the player's deck
assert len(plyr_test_deck.cards_in_hand) == 0   #confirming the initial list length of the player's hand

new_game.draw_card(plyr_test_deck.cards_in_hand, plyr_test_deck.cards) #passing cards in the player's hand
                                                                       #and the cards in deck into the draw_card function
new_game.draw_card(opp_test_deck.cards_in_hand, opp_test_deck.cards)   #passing cards in the opponent's hand
                                                                       #and the cards in deck into the draw_card function

assert len(plyr_test_deck.cards) == 19          #asserting that 1 card has been removed from the player's deck
assert len(plyr_test_deck.cards_in_hand) == 1   #asserting that 1 card from the player's deck has been moved into their hand
assert len(opp_test_deck.cards) == 19           #asserting that 1 card has been removed from the opponent's deck
assert len(opp_test_deck.cards_in_hand) == 1    #asserting that 1 card from the opponent's deck has been moved into their hand
assert plyr_test_deck.cards_in_hand[0].damage   #asserting that the creature card in teh player's hand has been assigned the correct values


new_game.draw_card(plyr_test_deck.cards_in_hand, plyr_test_deck.cards)  #drawing 20 cards (more than the amount in the deck list)
new_game.draw_card(plyr_test_deck.cards_in_hand, plyr_test_deck.cards)
new_game.draw_card(plyr_test_deck.cards_in_hand, plyr_test_deck.cards)
new_game.draw_card(plyr_test_deck.cards_in_hand, plyr_test_deck.cards)
new_game.draw_card(plyr_test_deck.cards_in_hand, plyr_test_deck.cards)
new_game.draw_card(plyr_test_deck.cards_in_hand, plyr_test_deck.cards)
new_game.draw_card(plyr_test_deck.cards_in_hand, plyr_test_deck.cards)
new_game.draw_card(plyr_test_deck.cards_in_hand, plyr_test_deck.cards)
new_game.draw_card(plyr_test_deck.cards_in_hand, plyr_test_deck.cards)
new_game.draw_card(plyr_test_deck.cards_in_hand, plyr_test_deck.cards)
new_game.draw_card(plyr_test_deck.cards_in_hand, plyr_test_deck.cards)
new_game.draw_card(plyr_test_deck.cards_in_hand, plyr_test_deck.cards)
new_game.draw_card(plyr_test_deck.cards_in_hand, plyr_test_deck.cards)
new_game.draw_card(plyr_test_deck.cards_in_hand, plyr_test_deck.cards)
new_game.draw_card(plyr_test_deck.cards_in_hand, plyr_test_deck.cards)
new_game.draw_card(plyr_test_deck.cards_in_hand, plyr_test_deck.cards)
new_game.draw_card(plyr_test_deck.cards_in_hand, plyr_test_deck.cards)
new_game.draw_card(plyr_test_deck.cards_in_hand, plyr_test_deck.cards)
new_game.draw_card(plyr_test_deck.cards_in_hand, plyr_test_deck.cards)
new_game.draw_card(plyr_test_deck.cards_in_hand, plyr_test_deck.cards)

assert len(plyr_test_deck.cards) == 0           #asserting cards can't be drawn out of the empty deck list
assert len(plyr_test_deck.cards_in_hand) == 20  #asserting the player's hand has all teh cards from their deck.

plyr_test_deck.__init__()     #resetting the player's deck
opp_test_deck.__init__()      #resetting the opponent's deck
new_game.__init__()           #resetting the game engine
plyr_test_deck.create_deck()  #creating the player's deck
opp_test_deck.create_deck()   #creating the opponent's deck

#testing play_resource():
    #drawing 2 resources and 3 creatures from the player's deck into their hand
plyr_test_deck.cards_in_hand.insert(0, plyr_test_deck.cards[9])
plyr_test_deck.cards_in_hand.insert(0, plyr_test_deck.cards[10])
plyr_test_deck.cards_in_hand.insert(0, plyr_test_deck.cards[0])
plyr_test_deck.cards_in_hand.insert(0, plyr_test_deck.cards[1])
plyr_test_deck.cards_in_hand.insert(0, plyr_test_deck.cards[2])

    #removing the cards from the player's deck which were put in their hand
plyr_test_deck.cards.remove(plyr_test_deck.cards[9])
plyr_test_deck.cards.remove(plyr_test_deck.cards[10])
plyr_test_deck.cards.remove(plyr_test_deck.cards[0])
plyr_test_deck.cards.remove(plyr_test_deck.cards[1])
plyr_test_deck.cards.remove(plyr_test_deck.cards[2])

assert len(plyr_test_deck.cards) == 15
# list_position = 0
# print("\n creature damages in hand \n")
# for card in plyr_test_deck.cards_in_hand:
#     if type(card) == Creature:
#         print(plyr_test_deck.cards_in_hand[list_position].damage)
#     list_position += 1
    

# list_position = 0
# print("\n creature damages in deck \n")
# for card in plyr_test_deck.cards:
#     if type(card) == Creature:
#         print(plyr_test_deck.cards[list_position].damage)
#     list_position += 1


    #asserting there are 3 creatures and 2 resources in the player's hand
assert type(plyr_test_deck.cards_in_hand[0]) == Creature
assert type(plyr_test_deck.cards_in_hand[1]) == Creature
assert type(plyr_test_deck.cards_in_hand[2]) == Creature
assert type(plyr_test_deck.cards_in_hand[3]) == Resource
assert type(plyr_test_deck.cards_in_hand[4]) == Resource

new_game.play_resources(plyr_test_deck.cards_in_hand, plyr_test_deck.resources_in_play)

assert len(plyr_test_deck.resources_in_play) == 2            #asserting the resource cards are in play
assert len(plyr_test_deck.cards_in_hand) == 3                #asserting the resource cards have been removed from the player's hand
assert type(plyr_test_deck.resources_in_play[0]) == Resource #asserting the resource cards are in play
assert type(plyr_test_deck.resources_in_play[1]) == Resource #asserting the resource cards are in play

#testing play_creature():
    #sending the player's hand, battlefield, resources in play, and discard pile into the function that plays a creature
new_game.play_creature(plyr_test_deck.cards_in_hand, plyr_test_deck.battlefield,\
                       plyr_test_deck.resources_in_play, plyr_test_deck.discard_pile) 

assert len(plyr_test_deck.cards_in_hand) == 1     #asserting there is 1 card left in the player's hand
assert len(plyr_test_deck.battlefield) == 2       #asserting there are now 2 cards on the player's battlefield
assert len(plyr_test_deck.resources_in_play) == 0 #asserting all the resources have been used
assert len(plyr_test_deck.discard_pile) ==  2     #asserting the discard pile has 2 cards

assert type(plyr_test_deck.cards_in_hand[0]) == Creature #asserting the 1 card in the player's hand is a creature
assert type(plyr_test_deck.battlefield[0]) == Creature   #asserting the 1st card on the player's battlefield is a creature
assert type(plyr_test_deck.battlefield[1]) == Creature   #asserting the 2nd card on the player's battlefield is a creature
assert type(plyr_test_deck.discard_pile[0]) == Resource  #asserting the 1st card in the discard pile is a resource
assert type(plyr_test_deck.discard_pile[1]) == Resource  #asserting the 2nd card in the discard pile is a resource

#testing attacking()
    #testing attacks on the opponent
assert new_game.new_opp.lp == 10 #asserting the opponent's health is 10 to start with

new_game.attacking(plyr_test_deck.battlefield, new_game.new_opp) #attacking the opponent with the creatures on the player's battlefield

assert plyr_test_deck.battlefield[0].damage == 1   #verifying the damage stat of the 1st creature on the player's field
assert plyr_test_deck.battlefield[1].damage == 2   #verifying the damage stat of the 2nd creature on the player's field

assert new_game.new_opp.lp == 7 #asserting the opponent's life points have dropped by 3 based on the attacks of the creatures on the player's battlefield

new_game.attacking(plyr_test_deck.battlefield, new_game.new_opp) #attacking the opponent with the creatures on the player's battlefield

assert new_game.new_opp.lp == 4 #asserting the opponent's life points have, again, dropped by 3 based on the attacks of the creatures on the player's battlefield


#Testing updating_the_board():
plyr_test_deck.__init__()     #resetting the player's deck
opp_test_deck.__init__()      #resetting the opponent's deck
new_game.__init__()           #resetting the game engine
plyr_test_deck.create_deck()  #creating the player's deck
opp_test_deck.create_deck()   #creating the opponent's deck

assert new_game.board == "" #checking the initial value given to the board

    #drawing 2 resources and 3 creatures from the player's deck into their hand
plyr_test_deck.cards_in_hand.insert(0, plyr_test_deck.cards[9])
plyr_test_deck.cards_in_hand.insert(0, plyr_test_deck.cards[10])
plyr_test_deck.cards_in_hand.insert(0, plyr_test_deck.cards[0])
plyr_test_deck.cards_in_hand.insert(0, plyr_test_deck.cards[1])
plyr_test_deck.cards_in_hand.insert(0, plyr_test_deck.cards[2])

    #removing the cards from the player's deck which were put in their hand
plyr_test_deck.cards.remove(plyr_test_deck.cards[9])
plyr_test_deck.cards.remove(plyr_test_deck.cards[10])
plyr_test_deck.cards.remove(plyr_test_deck.cards[0])
plyr_test_deck.cards.remove(plyr_test_deck.cards[1])
plyr_test_deck.cards.remove(plyr_test_deck.cards[2])

res_count = 0
for card in plyr_test_deck.cards_in_hand:   #counting the resources in the player's hand
    if type(card) == Resource:
        res_count += 1

assert res_count == 2 #asserting there are 2 resources in the player's hand

    #updating the board
new_game.updating_the_board(plyr_test_deck, opp_test_deck, \
                            new_game.new_plyr, new_game.new_opp)

print("\nPRINT 1" + new_game.board) #PRINT 1
"""PRINT 1 should show these values: (layout below is a rough copy)
=========================================================

         Cards In Hand:
    Resources: 0
Life (heart emoji): 10
                                        Deck: 20
            
---------------------------------------------------------

                                        Deck: 15
Life (heart emoji): 10
    Resources: 
         Cards In Hand: (card emoji) (card emoji) (card emoji) (card emoji) (card emoji)
         
=========================================================
"""

    #drawing 2 resources and 4 creatures from the opponent's deck into their hand
opp_test_deck.cards_in_hand.insert(0, opp_test_deck.cards[9])
opp_test_deck.cards_in_hand.insert(0, opp_test_deck.cards[10])
opp_test_deck.cards_in_hand.insert(0, opp_test_deck.cards[0])
opp_test_deck.cards_in_hand.insert(0, opp_test_deck.cards[1])
opp_test_deck.cards_in_hand.insert(0, opp_test_deck.cards[2])
opp_test_deck.cards_in_hand.insert(0, opp_test_deck.cards[3])

    #removing the cards from the opponent's deck which were put in their hand
opp_test_deck.cards.remove(opp_test_deck.cards[9])
opp_test_deck.cards.remove(opp_test_deck.cards[10])
opp_test_deck.cards.remove(opp_test_deck.cards[0])
opp_test_deck.cards.remove(opp_test_deck.cards[1])
opp_test_deck.cards.remove(opp_test_deck.cards[2])
opp_test_deck.cards.remove(opp_test_deck.cards[3])

new_game.play_resources(plyr_test_deck.cards_in_hand, plyr_test_deck.resources_in_play) #playing the player's resources 2 resources
new_game.play_resources(opp_test_deck.cards_in_hand, opp_test_deck.resources_in_play) #playing the opponent's resources 2 resources

new_game.play_creature(opp_test_deck.cards_in_hand, opp_test_deck.battlefield, \
                       opp_test_deck.resources_in_play, opp_test_deck.discard_pile) #playing the opponent's creatures


new_game.new_plyr.lp = 5
new_game.new_opp.lp = 7

    #updating the board
new_game.updating_the_board(plyr_test_deck, opp_test_deck, \
                            new_game.new_plyr, new_game.new_opp)

print("\nPRINT 2" + new_game.board) #PRINT 2


"""PRINT 2 should show these values: (layout below is a rough copy)
=========================================================

         Cards In Hand: (card emoji) (card emoji)
    Resources: 0
Life (heart emoji): 7
                                        Deck: 14
            (card emoji) (card emoji)
---------------------------------------------------------

                                        Deck: 15
Life (heart emoji): 5
    Resources: 2
         Cards In Hand: (card emoji) (card emoji) (card emoji)
         
=========================================================
"""

print("""
      All tests passed!""")

