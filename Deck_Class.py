# NAME: Dominic Walters


from Card_Class import Card
from Creature_Class import Creature
from Equipment_Class import Equipment
from Resource_Class import Resource
from Spell_Class import Spell

from random import shuffle

class Deck:
    def __init__(self):
        #assigning the appropriate classes to the card variables
        self.creature_1 = Creature()
        self.creature_2 = Creature()
        self.creature_3 = Creature()
        self.creature_4 = Creature()
        self.creature_5 = Creature()
        self.creature_6 = Creature()
        self.creature_7 = Creature()
        self.creature_8 = Creature()
        self.resource_1 = Resource()
        self.resource_2 = Resource()
        self.resource_3 = Resource()
        self.resource_4 = Resource()
        self.resource_5 = Resource()
        self.resource_6 = Resource()
        self.resource_7 = Resource()
        self.resource_8 = Resource()
        self.destroy_spell = Spell()
        self.block_spell = Spell()
        self.sword_equip = Equipment()
        self.shield_equip = Equipment()
        
        self.cards_in_hand = []
        self.discard_pile = []
        self.battlefield = []
        self.resources_in_play = []
        
        #creating the lists of cards
        self.creatures = [self.creature_1, self.creature_2, self.creature_3, self.creature_4, 
                          self.creature_5, self.creature_6, self.creature_7, self.creature_8]
        self.resources = [self.resource_1, self.resource_2, self.resource_3, self.resource_4, 
                          self.resource_5, self.resource_6, self.resource_7, self.resource_8]
        self.spells = [self.destroy_spell, self.block_spell]
        self.equips = [self.sword_equip, self.shield_equip]
        self.cards = [self.creature_1, self.creature_2, self.creature_3, self.creature_4, 
                      self.creature_5, self.creature_6, self.creature_7, self.creature_8,
                      self.resource_1, self.resource_2, self.resource_3, self.resource_4, 
                      self.resource_5, self.resource_6, self.resource_7, self.resource_8, 
                      self.destroy_spell, self.block_spell, self.sword_equip, self.shield_equip]
    
    def shuffle(self):
        pass
    
    #creates a deck
    def create_deck(self):
        
        #variables for the list position indicators
        creatures_position = 1
        resource_position = 1
        spells_position = 1
        equips_position = 1
        
        
        #loop to create each creature card in self.creatures
        for creature_card in self.creatures:
            # #prints the loop position
            # print(f"{creatures_position} of {len(self.creatures)} creatures")
            
            #assigns the damage and defense to the creature card
            if creatures_position == 1:
                creature_card.damage = 3
                creature_card.defense = 1
            elif creatures_position == 2:
                creature_card.damage = 1
                creature_card.defense = 3
            elif creatures_position == 3:
                creature_card.damage = 2
                creature_card.defense = 2
            elif creatures_position == 4:
                creature_card.damage = 2
                creature_card.defense = 1
            elif creatures_position == 5:
                creature_card.damage = 1
                creature_card.defense = 2
            else:
                creature_card.damage = 1
                creature_card.defense = 1
            
            #names the creature using the creatures_position variable as the creature's number
            creature_card.name = f"creature_{creatures_position}"
                
            #assigns resource cost to the card based on the damage and defense inputs:
            if creature_card.damage == 3 or creature_card.defense == 3:
                creature_card.resource_cost = 3
            elif creature_card.damage == 2 and creature_card.defense == 2:
                creature_card.resource_cost = 3
            elif creature_card.damage == 2 and creature_card.defense == 1:
                creature_card.resource_cost = 2
            elif creature_card.damage == 1 and creature_card.defense == 2:
                creature_card.resource_cost = 2
            else:
                creature_card.resource_cost = 1    
                
            #increments the list position placeholder
            creatures_position += 1
            
        #loop to create each resource card
        for resource_card in self.resources:
            # #prints the loop position
            # print(f"{resource_position} of {len(self.resources)} resources")
            resource_card.resource_amount = 1
            resource_card.resource_cost = 0
            resource_card.name = f"Resource {resource_position}"
            
            #increments the list position placeholder
            resource_position += 1
        
        
        #loop to create each spell card
        for spell_card in self.spells:
            # #prints the loop position
            # print(f"{spells_position} of {len(self.spells)} spells")
            
            #assigns resource cost
            spell_card.resource_cost = 1
            
            #names and provides spell type
            if spells_position == 1:
                spell_card.name = "Destruction"
                spell_card.block_card = False
                spell_card.destroy_card = True
            elif spells_position == 2:
                spell_card.name = "Block"
                spell_card.block_card = True
                spell_card.destroy_card = False
            else:
                None
            
            #increments the list position placeholder
            spells_position += 1
        
        #loop to create each equipment card
        for equip_card in self.equips:
            # #prints the loop position
            # print(f"{equips_position} of {len(self.equips)} equipment")
            
            #names and provides equipment buffs/types
            if equips_position == 1:
                equip_card.name = "Sword"
                equip_card.sword = True
                equip_card.shield = False
                equip_card.sword_buff = 1
                equip_card.shield_buff = 0
            elif equips_position == 2:
                equip_card.name = "Shield"
                equip_card.sword = False
                equip_card.shield = True
                equip_card.sword_buff = 0
                equip_card.shield_buff = 1
            else:
                None
            
            #increments the list position placeholder
            equips_position += 1   
        
        return




