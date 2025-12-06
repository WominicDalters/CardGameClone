# NAME: Dominic Walters


from Player_Class import Player

from Card_Class import Card
from Creature_Class import Creature
from Resource_Class import Resource
from Spell_Class import Spell
from Equipment_Class import Equipment

class Game_engine: #attributes
    rules = """\n
               
                    In this one on one card game, players are tasked \n
                    with bringing the other player's life points to zero.\n
                    Both sides start with 10 life points and 20 cards.\n
                    The decks consist of 8 resource, 8 creature, 2 spells\n
                    and 2 equipment. Each player can have a maximum of 3\n
                    3 creatures on the field at a time.\n\n
               
                    TURNS:\n\n
                    "Draw Phase"\n
                    Turns start with the first player drawing a card \n
                    from their deck.\n\n
               
                    "Setup Phase":\n
                    A resource card is played, then a creature card,\n
                    a spell card, and an equipment card.\n
                    To play any spell, creature or equipment you need to\n
                    have the resource amount required on the card.\n\n
               
                    "attack/Defense Phase"\n
                    The player is allowed to attack or defend for the turn,\n
                    attacking cards must have a cumulative attack stat\n
                    higher than the defense stat of the opponent's defending\n
                    card(s) to destroy them.\n
                    Similarly, a defending card must have a higher defence stat\n
                    than the attacking card(s) cumulative attack stat(s).\n
                    if there are no defencing creatures on the field,\n
                    the attacking creatures will attack the opponent's\n
                    life stat directly\n
                    Each creature can only attack once per turn.\n\n
               
                    "End Phase":\n
                    The turn ends.\n\n
                    """
    def __init__(self):
        self.new_plyr = Player()
        self.new_opp = Player()
        
        self.card_destroyed = False
        self.name = ""
        self.new_plyr.name = self.name
        self.new_opp.name = "Seto Kaiba"
        self.game_started = False
        self.game_over = False
        self.winner = None
        self.board = ""
       
    #methods, actions
    def setup_game(self):
        self.getting_player_name()
        self.explaining_rules()
        self.starting_game()
        return
        
    def getting_player_name(self):
        self.new_plyr.name = input("What is your name?: ")
        print(f"Hello there, {self.new_plyr.name} ")
        return self.new_plyr.name
    
    def explaining_rules(self):
        get_rules = "These are the rules: \n\n" + self.rules
        print(get_rules)
        
    
    def starting_game(self):
        self.game_started = True
        print("Link Start...")
    
    def dealing_cards(self, plyr_deck, opp_deck):                  #OPTIONAL
        pass
    
    #TURN CONTROLS
    def draw_card(self, cards_in_hand, deck):                      #DUE
        if len(deck) > 0:
            print("\nDrawing a card")
            cards_in_hand.insert(0, deck.pop(0))
    
    def play_resources(self, cards_in_hand, resources_in_play):     #DUE
        resources_to_remove = [] #a list to hold the cards that are being removed from cards_in_hand
        print("\nPlaying resources in hand\n")
        for card in cards_in_hand:
            if type(card) == Resource:
                resources_in_play.insert(0, card) #moves resources from the player's hand into resources_in_play
                resources_to_remove.append(card)  #sends the card to the list of cards that will be removed from the player's hand
        
        for card in resources_to_remove:          
            cards_in_hand.remove(card) #removes the cards from the hand that were put into resources_in_play
                
    
    def play_creature(self, cards_in_hand, battlefield, \
                      resources_in_play, discard_pile):             #DUE
        creatures_to_remove = []
        print("\nPlaying a creature\n")
        for card in cards_in_hand:
            if type(card) == Creature and len(resources_in_play) >= 1: #runs the code below if the player has a resource and a creature in hand
                battlefield.insert(0, card)       #moves creatures from the player's hand onto the battlefield
                self.discard_a_card(discard_pile, resources_in_play) #sends the used resource to the discard pile
                creatures_to_remove.append(card)  #adds the card to the list of cards to remove from the player's hand
                
        for card in creatures_to_remove:          
            cards_in_hand.remove(card) #removes the cards from the hand that were put on the battlefield
             
    def discard_a_card(self, discard_pile, set_of_cards):
        discard_pile.insert(0, set_of_cards.pop(0)) #adds the first card in the provided list to the discard pile
    
    def play_spell(self):
        pass
    
    def play_equipment(self):
        pass
    
    def attacking(self, battlefield, enemy_life):                     #DUE
        print("\nAttacking\n")
        for card in battlefield:
            if type(card) == Creature:
                enemy_life.lp -= card.damage #subtracting the damage from the enemy health
                if enemy_life.lp < 0:
                    enemy_life.lp = 0
                    
    def play_equipment(self, cards_in_hand, battlefield):
        equipment_to_remove = []
        print("\nPlaying equipment\n")
        for card in cards_in_hand:
            if type(card) == Equipment:  # only play equipment cards during turn
                battlefield.insert(0, card)
                equipment_to_remove.append(card)
                break  # break after playing the first equipment card
        
        for card in equipment_to_remove:          
            cards_in_hand.remove(card)
              
    
    def end_turn(self, plyr_deck, opp_deck):                                            #DUE
        print("End of Turn")
        self.checking_for_gameover(plyr_deck, opp_deck)
    
    def controlling_opponents(self):
        pass
    
    def updating_the_board(self, plyr_with_deck_class, opp_with_deck_class, \
                           plyr_lp, opp_lp):  #takes the player's deck class and opponent's deck class              #DUE
                                              #and player's Player class and opponent's Player class respectively                                        
        plyr_deck_txt = f"Deck: {len(plyr_with_deck_class.cards)}"
        opp_deck_txt = f"Deck: {len(opp_with_deck_class.cards)}"
        
        plyr_hand_txt = "Cards In Hand: "
        for card in plyr_with_deck_class.cards_in_hand:
            plyr_hand_txt += "|" + "\U0001F0CF" + card.name + "| "
        opp_hand_txt = "Cards In Hand: "
        for card in opp_with_deck_class.cards_in_hand:
            opp_hand_txt += "\U0001F0CF"
            
        plyr_lp_txt = "Life " + "\U0001F497" + ": " + str(plyr_lp.lp)
        opp_lp_txt = "Life " + "\U0001F497" + ": " + str(opp_lp.lp)
        
        plyr_field_txt = ""
        for card in plyr_with_deck_class.battlefield:
            plyr_field_txt += "\U0001F0CF"
        opp_field_txt = ""
        for card in opp_with_deck_class.battlefield:
            opp_field_txt += "\U0001F0CF"
        
        plyr_resources_txt = f"Resources: {len(plyr_with_deck_class.resources_in_play)}"
        opp_resources_txt = f"Resources: {len(opp_with_deck_class.resources_in_play)}"

       
        self.board = (
                "\n" + "Board: \n" +
                "====================================\n" +
                "\n        " + opp_hand_txt + "\n" +
                "    " + opp_resources_txt +  "\n" +
                opp_lp_txt + "\n" +
                "                                " + opp_deck_txt + "\n\n" +
                "             " + opp_field_txt + "\n" +
                "------------------------------------\n" +
                "             " + plyr_field_txt + "\n\n" +
                "                                " + plyr_deck_txt + "\n" +
                plyr_lp_txt + "\n" +
                "    " + plyr_resources_txt + "\n" +
                "        " + plyr_hand_txt + "\n\n" +
                "====================================\n") 
        
    def determining_the_winner(self):
        if self.game_over == True:
            if self.new_opp.lp <= 0 and self.new_plyr.lp <= 0:
                print("There has been an error determining the winner")
                self.winner = None
            elif self.new_plyr.lp <= 0:
                print("It seems you've lost, try again next time")
                self.winner = False
            elif self.new_opp.lp <= 0:
                print("Congrats on your victory!")
                self.winner = True
            else:
                print("There has been an error determining the winner")
                self.winner = None
        else:
            pass
        return
    
    def checking_for_gameover(self,plyr_deck, opp_deck):
        if self.new_plyr.lp <= 0 or self.new_opp.lp <= 0:
            self.game_over = True
            print("Game Over")
            self.game_started = False
        if len(plyr_deck.cards) < 1 or len(opp_deck.cards) < 1:
            self.game_over = True
            print("Game Over")
            self.game_started = False
        else:
            self.game_over = False
            print("the battle rages on... ")
        self.determining_the_winner()
        return
        
            

               


