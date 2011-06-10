from tronverse.Color import Color
from tronverse.Heading import Heading

class LightCycle(object):
    '''
    Light cycle vehicle
    '''
    
    def __init__(self, Color, Direction = Heading.NORTH, StartX = 0, StartY = 0):
        '''
        Initializes a new instance of the LightCycle class.
        '''
        
        self.RibbonColor = Color
        self.Direction = Direction
        self._LightRibbon = [(StartX, StartY)]
        self._Speed = 4
    
    def ChangeDirection(self, NewHeading):
        '''
        Change light cycle direction.
        '''
        
        # Check to make sure the bike is not pulling a 180 degree turn.
        if ((self.Direction == Heading.NORTH and NewHeading == Heading.SOUTH)
            or (self.Direction == Heading.SOUTH and NewHeading == Heading.NORTH)
            or (self.Direction == Heading.EAST and NewHeading == Heading.WEST)
            or (self.Direction == Heading.WEST and NewHeading == Heading.EAST)):
            pass
        else:
            self.Direction = NewHeading
    
    def CollisionWithLightRibbon(self, Ribbon):
        '''
        Check each point of a ribbon if we have a collision.
        '''
        
        for coord in Ribbon:
            if self._LightRibbon.count(coord) > 0:
                return True
        
        return False
    
    def CollisionWithWall(self, PosX, PosY):
        '''
        Check all possible wall collision combinations.
        '''
        
        # First find the current position.
        currentPosition = self._LightRibbon[-1]
        
        return ((currentPosition[0] < 1 or currentPosition[0] >= PosX)
                or (currentPosition[1] < 1 or currentPosition[1] >= PosY)
                or (self._LightRibbon.count(currentPosition) > 1))
    
    def LightRibbon(self):
        '''
        Return all vertices of the light ribbon.
        '''
        
        return self._LightRibbon[:]
    
    def Move(self):
        '''
        Move the light cycle one unit in its current direction.
        '''
        
        # First find the current position.
        currentPosition = self._LightRibbon[-1]
        
        # Determine which direction to move.
        if self.Direction == Heading.NORTH:
            self._LightRibbon.append((currentPosition[0], currentPosition[1] - self._Speed))
        elif self.Direction == Heading.EAST:
            self._LightRibbon.append((currentPosition[0] + self._Speed, currentPosition[1]))
        elif self.Direction == Heading.SOUTH:
            self._LightRibbon.append((currentPosition[0], currentPosition[1] + self._Speed))
        else:
            self._LightRibbon.append((currentPosition[0] - self._Speed, currentPosition[1]))
        
        # Return the light ribbon.
        return self._LightRibbon
    
    def SetSpeed(self, NewSpeed):
        self._Speed = NewSpeed