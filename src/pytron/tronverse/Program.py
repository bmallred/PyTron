from tronverse.Color import Color
from tronverse.LightCycle import LightCycle

class Program(object):
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

        color = Color.RED

        if self._Id == 0:
            color = Color.RED
        elif self._Id == 1:
            color = Color.BLUE
        elif self._Id == 2:
            color = Color.GREEN
        elif self._Id == 3:
            color = Color.YELLOW
        elif self._Id == 4:
            color = Color.WHITE

        self.LightCycle = LightCycle(color, Direction, StartX, StartY)