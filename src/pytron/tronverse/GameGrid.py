import pygame
from pygame.locals import *
from tronverse.Color import Color
from tronverse.Heading import Heading

class GameGrid(object):
    '''
    The Game Grid is where programs compete for their survival.
    '''
    
    def __init__(self, Width, Height):
        '''
        Initializes a new instance of the GameGrid class.
        '''
        
        # Initialize the game grid.
        self.Height = Height
        self.Width = Width
        self._FrameRate = 30
        self._Programs = []
        
        # Initialize pyGame.
        pygame.init()
        pygame.display.set_caption("PyTron")
        self._Clock = pygame.time.Clock()
        self._Screen = pygame.display.set_mode((self.Width, self.Height))
        self._Background = pygame.Surface(self._Screen.get_size())
        self._Background.fill(Color.BLACK)
    
    def DoWork(self):
        # Tick-Tock.
        self._Clock.tick(self._FrameRate)
        
        # Clear screen (or possibly don't?).
        self._Screen.blit(self._Background, (0, 0))
        
        # Peek at inputs.
        self._HandleEvents(pygame.event.get())
        
        for prog in self._Programs:
            # Move and draw.
            self._DrawLightRibbon(prog.LightCycle.Move(), prog.LightCycle.RibbonColor)
            
            # Collision checking.
            if prog.LightCycle.CollisionWithWall(self.Width, self.Height):
                if prog.Derezz():
                    self._Programs.remove(prog)
            else:
                # For each opponent check if program collided with their light ribbon.
                # If so, determine if program should derezz.
                
                for opponent in self._Opponents(prog):
                    if prog.LightCycle.CollisionWithLightRibbon(opponent.LightCycle.LightRibbon()):
                        if prog.Derezz():
                            self._Programs.remove(prog)
        
        # Flip! Flip! (i.e. update the display with the latest changes)
        pygame.display.flip()
    
    def IsRunning(self):
        '''
        Returns a value indicating whether the game is still running.
        '''
        
        return len(self._Programs) > 1
    
    def LoadProgram(self, Program):
        '''
        Load a program in to the game grid.
        '''
        
        self._Programs.append(Program)
    
    def SetFrameRate(self, Rate):
        '''
        Sets the frame rate.
        '''
        
        self._FrameRate = Rate
    
    def _DrawLightRibbon(self, Vertices, Color = Color.RED):
        '''
        Draws the light ribbon.
        '''
        
        pygame.draw.lines(self._Screen, Color, False, Vertices, 1)
    
    def _HandleEvents(self, Events):
        '''
        Handles input events from the user(s).
        '''
        
        # TODO: Do not make static!!!!
        # Need to do something cool so there can be more
        # than just two programs playing (possibly use Id).
        
        # TODO: Add pause handling (i.e. K_SPACE).
        # TODO: Add additional exit handling (i.e. K_ESCAPE).
        # TODO: Add speed handling per program.
        
        for e in Events:
            if e.type == QUIT:
                self._Programs = []
                #pygame.quit()
            elif e.type == KEYDOWN:
                # Program one navigation.
                if e.key == K_a:
                    self._Programs[0].LightCycle.ChangeDirection(Heading.WEST)
                elif e.key == K_s:
                    self._Programs[0].LightCycle.ChangeDirection(Heading.SOUTH)
                elif e.key == K_d:
                    self._Programs[0].LightCycle.ChangeDirection(Heading.EAST)
                elif e.key == K_w:
                    self._Programs[0].LightCycle.ChangeDirection(Heading.NORTH)
                
                # Program two navigation.
                elif e.key == K_j:
                    self._Programs[1].LightCycle.ChangeDirection(Heading.WEST)
                elif e.key == K_k:
                    self._Programs[1].LightCycle.ChangeDirection(Heading.SOUTH)
                elif e.key == K_l:
                    self._Programs[1].LightCycle.ChangeDirection(Heading.EAST)
                elif e.key == K_i:
                    self._Programs[1].LightCycle.ChangeDirection(Heading.NORTH)
    
    def _Opponents(self, Program):
        '''
        Finds a programs opponents.
        '''
        
        opponents = self._Programs[:]
        opponents.remove(Program)
        
        return opponents