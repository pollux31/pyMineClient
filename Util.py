'''
Created on 14 juin 2014

@author: Thierry
'''

class Coord(object):
    """
    Manage coordinate
    """
    
    def __init__(self, x=0, y=0, z=0):
        '''
        Constructor
        '''
        self.x = x
        self.y = y
        self.z = z

    def SetCoord(self, x, y, z):
        """
        Set the new positoin of the player
        Coordonate are given by a Spawn Postion packet
        """
        self.x = x
        self.y = y
        self.z = z
        

     