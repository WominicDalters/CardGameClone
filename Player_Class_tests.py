from Player_Class import Player

#setting new_player as a Player Class
new_player = Player()

#testing lose_lp()

new_player.lose_lp(1)
assert new_player.lp == 9
new_player.lose_lp(11)
assert new_player.lp == 0

#testing gain_lp()
new_player.gain_lp(1)
assert new_player.lp == 1
new_player.gain_lp(11)
assert new_player.lp == 10

#testing is_alive()
    #resetting new_player's lp
new_player.lp = 10
assert new_player.is_alive() == True
    #resetting new_player's lp
new_player.lp = 0
assert new_player.is_alive() == False

#testing __init__()
new_player.__init__()
assert new_player.lp == 10
assert new_player.alive == True

print("All tests passed!")