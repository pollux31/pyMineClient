'''
Created on 14 juin 2014

@author: Thierry
'''

import  asyncio
from Network import Network

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    coro = loop.create_connection(Network, '127.0.0.1', 25565)
    loop.run_until_complete(coro)
    loop.run_forever()
    loop.close()
    
    
