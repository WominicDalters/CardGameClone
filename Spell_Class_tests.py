# NAME: Dominic Walters

from Spell_Class import Spell

#assigning Spell() to new_spell
new_spell = Spell()

#testing __init__()
    #changing initial variable values
new_spell.block_card = True
new_spell.destroy_card = True
assert new_spell.block_card == True
assert new_spell.destroy_card == True

new_spell.__init__()
assert new_spell.block_card == False
assert new_spell.destroy_card == False

print("All tests passed!")