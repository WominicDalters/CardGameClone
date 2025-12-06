# NAME: Dominic Walters


from Creature_Class import Creature

#assigning Creature() to new_cre
new_cre = Creature()

#testing __init__()
    #changing variable values
new_cre.damage = 5
new_cre.defense = 6
new_cre.creature_type = 7
assert new_cre.damage == 5
assert new_cre.defense == 6
assert new_cre.creature_type == 7
    #running __init__()
new_cre.__init__()
assert new_cre.damage == 0
assert new_cre.defense == 0
assert new_cre.creature_type == ""

print("All tests passed!")