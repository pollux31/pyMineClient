'''
Created on 22 juin 2014

@author: Thierry

Entities Management
'''

from Debug import Debug
from Util import Coord, Look



class Entity(object):
    """
    Management of an Entity
    """
    def __init__(self, id):
        self.id = id
        self.type = 0
        self.pos = Coord()
        self.yaw = 0
        self.pitch = 0
        
    def SetPos(self, x, y, z):
        self.pos.SetCoord(x, y, z)
    
    def Move(self, dx, dy, dz):
        self.pos.Offset(dx, dy, dz)

    def Look(self, yaw, pitch):
        self.yaw = 0
        self.pitch = 0
        
    def SetType(self,type):
        self.type = type
        
        

# ------------------------------------------------------------------
class Entities(object):
    """
    List of all Entities in the world
    """    
    def __init__(self, app):
        self.application = app
        self.entityList = {}        # dictionnay to store Entity objects


    def Entity(self, id):
        """ 
        Initialisation of an entity
        Entity can exists before this message
        """
        if id not in self.entityList:
            self.entityList[id] = Entity(id)
         
    
    def SetPos(self, id, x, y, z):
        """ Set the absolute position """
        if id not in self.entityList:
            Debug("Unknown Entity %d for new Position !" % id)
        else:
            Debug("For Entity %d, set Pos" % id)
            self.entityList[id].SetPos(x, y, z)
        
    def GetPos(self,id):
        if id not in self.entityList:
            Debug("Unknown Entity %d for GetPos !" % id)
        else:
            return self.entityList[id].pos

    def RelativeMove(self, id, dx, dy, dz):
        """ Move an Entity with a relative offset """
        if id not in self.entityList:
            Debug("Unknown Entity %d to move !" % id)
        else:
            self.entityList[id].Move(dx, dy, dz)


    def Look(self, id, yaw, pitch):
        """ chagne the look position """
        if id not in self.entityList:
            Debug("Unknown Entity %d for look update !" % id)
        else:
            self.entityList[id].Look(yaw, pitch)
            
    def SetType(self, id, type):
        if id not in self.entityList:
            Debug("Unknown Entity %d for set Type !" % id)
        else:
            self.entityList[id].SetType(type)
        