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


    def __init__(self, id):
        '''
        Constructor
        '''
        self.id = id
        self.name = ""
        self.position = Coord()
        self.positionAbs = Coord()
        self.health = 0
        self.food = 0
        self.playerList = {}


    def SetName(self, name):
        self.name = name
    
    def GetName(self):
        return self.name

    def GetPosition(self):
        return self.position
    
    def SetPosition(self, x, y, z):
        """
        Set the new position of the player
        Coordonate are given by a Spawn Postion packet
        """
        self.position.SetCoord(x, y, z)
        
    def SetAbsolutePosition(self, x, y, z):
        """
        Set the new absolute position of the player (eye position)
        Coordonate are given by a Spawn Postion packet
        """
        self.positionAbs.SetCoord(x, y, z)
        
    def SetHealth(self, h):
        self.health = h
        
    def SetFood(self, f):
        self.food = f
        
        


# --------------------------------------------------------------
class Players(object):
    """
    Manage the list of players
    """
    def __init__(self, app):
        self.application = app
        self.playerList = {}
        self.botId = None
        
    def SetBot(self, id, name):
        """ Initialise the Bot """
        self.botId = id
        self.AddPlayer(id, name)
        
    def AddPlayer(self, id, name):
        """ Add a new player in the Players list """
        if id not in self.playerList:
            self.playerList[id] = Player(id)
            self.playerList[id].SetName(name)

    def SetBotPosition(self, x, y, z):
        self.playerList[self.botId].SetPosition(x, y, z)

    def SetBotHealthFood(self, health, food):
        self.playerList[self.botID].SetHealth(health)
        self.playerFood[self.botID].SetFood(food)

    def SetBotAbsolutePosition(self, x, y, z):
        self.playerList[self.botId].SetAbsolutePosition(x, y, z)

    def SetPosition(self, id, x, y, z):
        if id not in self.playerList:
            Debug("Unknown Player %d for new Position !" % id)
        else:
            self.playerList[id].SetPosition(x, y, z)
            
    def GetPlayerId(self, name):
        """ Get the plyer ID corresponding to his name """
        player_id = None
        for id in self.playerList:
            if self.playerList[id].GetName() == name:
                player_id = id
                break
        return player_id



#     def ManageOtherPlayers(self, name, online):
#         """
#         manage the list of actif player
#         """
#         if online == True and name not in self.playerList:
#             self.playerList[name] = {}
#             print("Add player '%s' in the players list" % name)
#         elif name in self.playerList and online == False:
#             del self.playerList[name]
#             print("Add player '%s' in the players list" % name)

