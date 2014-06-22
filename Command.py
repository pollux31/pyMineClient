'''
Created on 14 juin 2014

@author: Thierry
'''

class Command(object):
    
    def __init__(self, app):
        self.application = app
        
        
    def DispatchCommand(self, txt, sender):
        """ Analyze the command and call the corresponding function """
        
        data = txt.split(' ')
        cmd = data[0].upper()
        
        if cmd == "MYPOS":
            self.PrintSenderPos(sender)
            
            
    def PrintSenderPos(self, sender):
        players = self.application.GetPlayers()
        entities = self.application.GetEntities()
        
        id = players.GetPlayerId(sender)
        if id == None:
            Debug('Player %s not found' % name)
        else:
            pos = entities.GetPos(id)
            print("Position de %s = (%f, %f, %f)" % (sender, pos.x, pos.y, pos.z))