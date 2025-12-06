from Resource_Class import Resource

#assigning Resource() to new_resource
new_resource = Resource()

#changing variable values
new_resource.resource_amount = 9
new_resource.resource_cost = 8
assert new_resource.resource_amount == 9
assert new_resource.resource_cost == 8

#testing __init__()
new_resource.__init__()
assert new_resource.resource_amount == 1
assert new_resource.resource_cost == 0

print("All tests passed!")