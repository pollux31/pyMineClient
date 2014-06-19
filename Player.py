'''
Created on 17 juin 2014

@author: Thierry
'''

class Player(object):
    '''
    Manage the Bot player
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.posX = 0
        self.posY = 0
        self.posZ = 0
        self.absPosX = 0
        self.absPosY = 0
        self.absPosZ = 0
        self.health = 0
        self.food = 0

    def SetPosition(self, x, y, z):
        """
        Set the new positoin of the player
        Coordonate are given by a Spawn Postion packet
        """
        self.posX = x
        self.posY = y
        self.posZ = z
        
    def SetAbsolutePosition(self, x, y, z):
        """
        Set the new absolute positoin of the player (eye position)
        Coordonate are given by a Spawn Postion packet
        """
        self.absPosX = x
        self.absPosY = y
        self.absPosZ = z
        
        
    def SetHealth(self, h):
        self.health = h
        
    def SetFood(self, f):
        self.food = f
