# NAME: Dominic Walters
# STUDENT NUMBER: 300196102
# UFV ID: dominic.walters@student.ufv.ca

from Equipment_Class import Equipment

#assigning Equipment() to new_eq
new_eq = Equipment()

#Testing __init__()
    #Changing initial variable values
new_eq.sword = True
new_eq.shield = True
new_eq.sword_buff = 7
new_eq.shield_buff = 8
assert new_eq.sword == True
assert new_eq.shield == True
assert new_eq.sword_buff == 7
assert new_eq.shield_buff == 8

new_eq.__init__()
assert new_eq.sword == False
assert new_eq.shield ==  False
assert new_eq.sword_buff == None
assert new_eq.shield_buff == None

print("All tests passed!")