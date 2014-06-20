'''
Created on 17 juin 2014

@author: Thierry
'''
from Util import Coord
from Chat import Chat

class Player(object):
    '''
    Manage the Bot player
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        self.position = Coord()
        self.positionAbs = Coord()
        self.health = 0
        self.food = 0

    def GetName(self):
        return self.name

    def SetPosition(self, x, y, z):
        """
        Set the new positoin of the player
        Coordonate are given by a Spawn Postion packet
        """
        self.position.SetCoord(x, y, z)
        
    def SetAbsolutePosition(self, x, y, z):
        """
        Set the new absolute positoin of the player (eye position)
        Coordonate are given by a Spawn Postion packet
        """
        self.positionAbs.SetCoord(x, y, z)
        
    def SetHealth(self, h):
        self.health = h
        
    def SetFood(self, f):
        self.food = f
        
    def ReadChat(self, msg):
        """
        get the JSON message and analyse it
        """
        chat = Chat(msg)
        
