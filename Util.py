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
        
    def Offset(self, dx, dy, dz):
        """
        Add the offset to the position
        """
        self.x += dx
        self.y += dy
        self.z += dz
        

class Look(object):
    """ 
    manage the player or entity look direction
    """
    def __init__(self, yaw=0, pitch=0):
        self.yaw = yaw
        self.pitch = pitch
        
    def SetLook(self, yaw, pitch):
        self.yaw = yaw
        self.pitch = pitch
        

     