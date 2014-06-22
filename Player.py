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


    def __init__(self, app, name):
        '''
        Constructor
        '''
        self.application = app
        self.name = name
        self.position = Coord()
        self.positionAbs = Coord()
        self.health = 0
        self.food = 0
        self.playerList = {}

    
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
        
    def ManageOtherPlayers(self, name, online):
        """
        manage the list of actif player
        """
        if online == True and name not in self.playerList:
            self.playerList[name] = {}
            print("Add player '%s' in the players list" % name)
        elif name in self.playerList and online == False:
            del self.playerList[name]
            print("Add player '%s' in the players list" % name)

    def SetOtherPlayerPosition(self, name, id, x, y, z):
        if id not in self.entityList:
            self.entityList.append({})
        self.playerList['id']['name'] = name
        self.playerList['id']['type'] = -1
        self.playerList['id']['pos'] = Coord(x, y, z)
        
