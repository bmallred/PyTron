from pytron.LightCycle import LightCycle

class Program:
    '''
    A user program
    '''
    
    def __init__(self, Id):
        '''
        Initializes a new instance of the Program class.
        '''
        
        self._Health = 1
        self._Id = Id
        self.LightCycle = None
    
    def Derezz(self):
        '''
        Returns a value indicating whether the program should derezz.
        '''
        
        # Decrease health by one.
        self._Health = self._Health - 1
        
        # Return boolean indicating whether to derezz the player.
        return self._Health == 0
    
    def Name(self):
        '''
        Returns the programs name.
        '''
        
        return "Player " + self._Id
    
    def UseBaton(self, Direction, StartX, StartY):
        '''
        Use the baton to generate the light cycle.
        '''
        
        self.LightCycle = LightCycle(self._Id, Direction, StartX, StartY)