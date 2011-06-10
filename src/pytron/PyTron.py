#!/usr/bin/python

from tronverse.Heading import Heading
from tronverse.Program import Program
from tronverse.GameGrid import GameGrid

def startGame():
    '''
    Start game play.
    '''
    
    #
    # Build the game grid.
    #
    
    gameGrid = GameGrid(640, 480)
    gameGrid.SetFrameRate(30)
    
    #
    # Create the programs (players).
    #
    
    clu = Program(0)
    clu.UseBaton(Heading.SOUTH, 10, 10)
    
    ram = Program(1)
    ram.UseBaton(Heading.NORTH, gameGrid.Width - 10, gameGrid.Height - 10)
    
    #
    # Load programs in to the game grid.
    #
    
    gameGrid.LoadProgram(clu)
    gameGrid.LoadProgram(ram)
    
    #
    # Engine.
    #
    
    while gameGrid.IsRunning():
        gameGrid.DoWork()

if __name__ == "__main__":
    startGame()
