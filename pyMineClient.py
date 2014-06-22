'''
Created on 14 juin 2014

@author: Thierry
'''

import  asyncio
from Network import Network
from Player import Player
from Entities import Entities
from Network import Network

class App(object):
    
    def __init__(self):
        # Create the Player management
        self.player = Player(self, 'Thierry')
        
        # Create the Entities management
        self.entities = Entities(self)
        
        # create the Network factory to handle packet exchanges with the server
        self.network = Network(self)


    def GetPlayer(self):
        """ get the player object """
        return self.player


    def GetEntities(self):
        """ return the enities object """
        return self.entities


    def Run(self):
        """ run the infinite loop to manage Server exchanges """
        loop = asyncio.get_event_loop()
        coro = loop.create_connection(lambda: self.network, '127.0.0.1', 25565)
        loop.run_until_complete(coro)
        loop.run_forever()
        loop.close()
    
    

if __name__ == '__main__':
    # create the application
    app = App()
    app.Run()
