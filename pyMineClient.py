'''
Created on 14 juin 2014

@author: Thierry
'''

import  asyncio
from Network import Network
from Player import Players
from Entities import Entities
from Network import Network
from Command import Command

class App(object):
    
    def __init__(self, name):
        self.botName = name
        # Create the Player management
        self.players = Players(self)
        
        # Create the Entities management
        self.entities = Entities(self)
        
        # create the Network factory to handle packet exchanges with the server
        self.network = Network(self, name)

        # create the command object
        self.command = Command(self)

    def GetBotName(self):
        """ return the Name of the Bot """
        return self.botName
    
    def GetPlayers(self):
        """ get the players list """
        return self.players

    def GetEntities(self):
        """ return the enities object """
        return self.entities

    def GetCommand(self):
        return self.command
    
    def Run(self):
        """ run the infinite loop to manage Server exchanges """
        loop = asyncio.get_event_loop()
        coro = loop.create_connection(lambda: self.network, '127.0.0.1', 25565)
        loop.run_until_complete(coro)
        loop.run_forever()
        loop.close()
    
    

if __name__ == '__main__':
    # create the application
    app = App('Thierry')
    app.Run()
