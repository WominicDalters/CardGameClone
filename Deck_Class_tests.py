# NAME: Dominic Walters


from Deck_Class import Deck
from Card_Class import Card
from Creature_Class import Creature
from Equipment_Class import Equipment
from Resource_Class import Resource
from Spell_Class import Spell

#assigning Deck() to the variable new_deck
new_deck = Deck()

#testing create_deck()
new_deck.create_deck()

    #verifying creature_1
assert new_deck.creature_1.damage == 3
assert new_deck.creature_1.defense == 1
assert new_deck.creature_1.name == "creature_1"
assert new_deck.creature_1.resource_cost == 3

    #verifying creature_2
assert new_deck.creature_2.damage == 1
assert new_deck.creature_2.defense == 3
assert new_deck.creature_2.name == "creature_2"
assert new_deck.creature_2.resource_cost == 3

    #verifying creature_3
assert new_deck.creature_3.damage == 2
assert new_deck.creature_3.defense == 2
assert new_deck.creature_3.name == "creature_3"
assert new_deck.creature_3.resource_cost == 3

    #verifying creature_4
assert new_deck.creature_4.damage == 2
assert new_deck.creature_4.defense == 1
assert new_deck.creature_4.name == "creature_4"
assert new_deck.creature_4.resource_cost == 2

    #verifying creature_5
assert new_deck.creature_5.damage == 1
assert new_deck.creature_5.defense == 2
assert new_deck.creature_5.name == "creature_5"
assert new_deck.creature_5.resource_cost == 2

    #verifying creature_6
assert new_deck.creature_6.damage == 1
assert new_deck.creature_6.defense == 1
assert new_deck.creature_6.name == "creature_6"
assert new_deck.creature_6.resource_cost == 1

    #verifying creature_7
assert new_deck.creature_7.damage == 1
assert new_deck.creature_7.defense == 1
assert new_deck.creature_7.name == "creature_7"
assert new_deck.creature_7.resource_cost == 1

    #verifying creature_8
assert new_deck.creature_8.damage == 1
assert new_deck.creature_8.defense == 1
assert new_deck.creature_8.name == "creature_8"
assert new_deck.creature_8.resource_cost == 1
    

    #verifying resource_1   
assert new_deck.resource_1.resource_amount == 1
assert new_deck.resource_1.resource_cost == 0
assert new_deck.resource_1.name == "Resource"

    #verifying resource_2   
assert new_deck.resource_2.resource_amount == 1
assert new_deck.resource_2.resource_cost == 0
assert new_deck.resource_2.name == "Resource"

    #verifying resource_3   
assert new_deck.resource_3.resource_amount == 1
assert new_deck.resource_3.resource_cost == 0
assert new_deck.resource_3.name == "Resource"

    #verifying resource_4   
assert new_deck.resource_4.resource_amount == 1
assert new_deck.resource_4.resource_cost == 0
assert new_deck.resource_4.name == "Resource"

    #verifying resource_5   
assert new_deck.resource_5.resource_amount == 1
assert new_deck.resource_5.resource_cost == 0
assert new_deck.resource_5.name == "Resource"

    #verifying resource_6   
assert new_deck.resource_6.resource_amount == 1
assert new_deck.resource_6.resource_cost == 0
assert new_deck.resource_6.name == "Resource"

    #verifying resource_7   
assert new_deck.resource_7.resource_amount == 1
assert new_deck.resource_7.resource_cost == 0
assert new_deck.resource_7.name == "Resource"

    #verifying resource_8   
assert new_deck.resource_8.resource_amount == 1
assert new_deck.resource_8.resource_cost == 0
assert new_deck.resource_8.name == "Resource"


    #verifying destroy_spell
assert new_deck.destroy_spell.name == "Destruction"
assert new_deck.destroy_spell.block_card == False
assert new_deck.destroy_spell.destroy_card == True
assert new_deck.destroy_spell.resource_cost == 1

    #verifying block_spell
assert new_deck.block_spell.name == "Block"
assert new_deck.block_spell.block_card == True
assert new_deck.block_spell.destroy_card == False
assert new_deck.block_spell.resource_cost == 1

    #verifying sword_equip
assert new_deck.sword_equip.name == "Sword"
assert new_deck.sword_equip.sword == True
assert new_deck.sword_equip.shield == False
assert new_deck.sword_equip.sword_buff == 1
assert new_deck.sword_equip.shield_buff == 0

    #verifying shield_equip
assert new_deck.shield_equip.name == "Shield"
assert new_deck.shield_equip.sword == False
assert new_deck.shield_equip.shield == True
assert new_deck.shield_equip.sword_buff == 0
assert new_deck.shield_equip.shield_buff == 1

print("All tests passed!")