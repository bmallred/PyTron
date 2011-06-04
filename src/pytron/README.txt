Program:	PyTron
Author:		Bryan M. Allred
Created:	06/03/2011

Dependencies:
	Python 2.7
	pygame

Description:
	Simple Tron game written in Python.

Acknowledgements:
	HacDC (http://www.hacdc.org) for the great introduction.
	Python documentation on classes.
	PEP008 "Style Guide for Python Code".
	Pygame documentation.
	Alec Thomas on the sweet Enum() function found on StackOverflow (I felt I needed enumerations!).

Directions:

Avoid hitting the game grids boundaries as well as each programs light ribbon. Currently each
programs health level is set to "1" so you only have one chance before derezz. To navigate your
light cycle use the following keys:

	Player 1 (Program "Clu")
		A -> Left
		S -> Down
		D -> Right
		W -> Up

	Player 2 (Program "Ram")
		J -> Left
		K -> Down
		L -> Right
		I -> Up

Issues:

[Unresolved] Once each programs light ribbon has reach a large number the redrawing of the screen
eats up resources. This causes a delay in reaction time and makes the game appear sluggish. Possibly
need to implement some sort of caching or only draw the new portions of the ribbon.

[Unresolved] Never got around to implementing different light cycle colors.

[Unresolved] Sound.