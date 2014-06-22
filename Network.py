'''
Created on 14 juin 2014

@author: Thierry

Network Factory

Manages the communication with the server in an Asyncio mode.
When the connection is done:
    - create the Protocol object
    - send the login request to the server 
'''

import asyncio
from Packet import Packet
from Debug import Debug
from Protocol import Protocol

class Network(asyncio.Protocol):

    def __init__(self, app):
        self.application = app
        self.player = self.application.GetPlayer()
        Debug("Network initialisation")

    
    def connection_made(self, transport):
        """ call when the connection with the server is done """
        self.transport = transport
    
        # Cnx ok, create the Protocol object
        Debug("Connexion ok")
        self.protocol = Protocol(self.application, transport)
        self.protocol.setStateLogin()
        
        # start the dialog
        self.protocol.Out('handshake', protocol_version=5, 
                          server_adress='localhost', server_port=25565, next_state=2)
        self.protocol.Out('login_start', name=self.player.GetName())    

    
    def data_received(self, data):
        """ 
        incoming data are ready 
        """
        
        # compute all packets
        while (len(data) > 0):
            packet = Packet(data)
            size   = packet.getVarint()
            offset = packet.getVarintSize()
            packet = Packet(data[offset:offset+size])
            
            # compute the packet
            self.protocol.Receive(packet)
            
            # remove the packet
            data = data[offset+size:]
        
        
    def connection_lost(self, exc):
        """
        the connection is closed
        """
        Debug('Server closed the connection')
        # stop the infinite loop
        asyncio.get_event_loop().stop()
