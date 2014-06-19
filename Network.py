'''
Created on 14 juin 2014

@author: Thierry
'''
import asyncio
from Packet import Packet
from Debug import Debug
from Protocol import Protocol

class Network(asyncio.Protocol):
    def __init__(self):
        self.recData = asyncio.Queue();
        self.protocol = Protocol(self)
        self.protocol.setStateLogin()
        Debug("Network initialisation")
    
    def connection_made(self, transport):
        self.transport = transport
        Debug("Connexion ok")
        # start the dialog
        self.protocol.Out('handshake', protocol_version=5, 
                          server_adress='localhost', server_port=25565, next_state=2)
        self.protocol.Out('login_start', name='Thierry')     # TODO: accept username as parameter !

    def data_received(self, data):
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
        Debug('Server closed the connection')
        asyncio.get_event_loop().stop()


    