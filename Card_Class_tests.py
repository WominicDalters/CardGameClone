# NAME: Dominic Walters


from Card_Class import Card

#assigning Card() to new_card
new_card = Card()

#testing __init__()
    #changing variable values
new_card.name = 1
new_card.description = 1
new_card.resource_cost = 1
new_card.destroyed = True
new_card.active = True
assert new_card.name == 1
assert new_card.description == 1
assert new_card.resource_cost == 1
assert new_card.destroyed == True
assert new_card.active == True

    #running __init__()
new_card.__init__()
assert new_card.name == ""
assert new_card.description == ""
assert new_card.resource_cost == None
assert new_card.destroyed == False
assert new_card.active == False

print("All tests passed!")