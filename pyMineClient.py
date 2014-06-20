'''
Created on 14 juin 2014

@author: Thierry
'''

import  asyncio
from Network import Network
from Player import Player
from Network import Network

if __name__ == '__main__':
    
    # Create the Player
    player = Player('Thierry')
    
    # create the Network factory to handle packet exchanges with the server
    network = Network(player)
    
    # intialisation of the infinite loop
    loop = asyncio.get_event_loop()
    coro = loop.create_connection(lambda: network, '127.0.0.1', 25565)
    loop.run_until_complete(coro)
    loop.run_forever()
    loop.close()
    
    
