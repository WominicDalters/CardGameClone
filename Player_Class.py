# NAME: Dominic Walters


class Player: #Attributes
    def __init__(self):
        self.alive = True
        self.lp = 10
 
    #Actions
    
    def lose_lp(self, dmg_taken):
       self.lp -= dmg_taken
       
       if self.lp < 0:
           self.lp = 0
       
       return self.lp
   
    def gain_lp (self, lp_gained):
        self.lp += lp_gained
        
        if self.lp > 10:
            self.lp = 10
        
        return self.lp
    
    def is_alive(self):
        if self.lp <= 0:
            self.alive = False
        else:
            self.alive = True
        return self.alive
    

