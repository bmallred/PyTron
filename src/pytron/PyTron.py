#!/usr/bin/python

from pytron.GameGrid import GameGrid
from pytron.Program import Program
from pytron.locals.Heading import Heading

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

gameGrid.LoadProgram(clu)
gameGrid.LoadProgram(ram)

#
# Engine.
#

while gameGrid.IsRunning():
    gameGrid.DoWork()

#
# End of the world.
#