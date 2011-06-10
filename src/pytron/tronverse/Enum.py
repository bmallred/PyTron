'''
Created on Nov 8, 2009

@author: Alec Thomas
'''

def Enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)