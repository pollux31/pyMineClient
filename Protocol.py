'''
Created on 15 juin 2014

@author: Thierry
'''

from Debug import Debug
from Packet import Packet
from Player import Player
from Chat import Chat
from DescProto import LOGIN_STATE, PLAY_STATE, STATUS_STATE, LOGIN_OUT, LOGIN_IN, STATUS_OUT, STATUS_IN, PLAY_OUT, PLAY_IN

class Protocol (object):
    def __init__(self, app, cnx):
        self.application = app
        self.cnx = cnx
        self.players = self.application.GetPlayers()
        self.entities = self.application.GetEntities()
        
    def setStateLogin(self):
        self.state = LOGIN_STATE
    def setStateStatus(self):
        self.state = STATUS_STATE
    def setStatePlay(self):
        self.state = PLAY_STATE
        
        
    def Send(self, packetID, data=None):
        """
        Send to the server the packet with the right format
        """
        tmp = []
        tmp.extend(Packet().toVarint(packetID))
        if (data != None):
            tmp.extend(data)
        buf = bytearray()
        buf.extend(Packet().toVarint(len(tmp)))
        buf.extend(tmp)
        self.cnx.write(buf)
        
        
    def Out(self, packetName, **kvargs):
        """
        Create a buffer with the packet data data
        name : name of the packet
        kvargs : list of packet parameters
        example -> Out('send_login', name='player1')
        """ 
        if (self.state == PLAY_STATE):
            tab = PLAY_OUT
        elif (self.state == LOGIN_STATE):
            tab = LOGIN_OUT
        elif (self.state == STATUS_STATE):
            tab = STATUS_OUT

        packetID = tab[packetName][0]
        param = tab[packetName][1]
        
        data = []
        for i in range(0, len(param), 2):
            val = kvargs[param[i]]
            # retreive the function to call to format the value
            buf = getattr(Packet(), 'to'+param[i+1])(val)
            data.extend(buf)  # add the buffer to the global data array
        
        # ready to send
        self.Send(packetID, data)
        

    def Receive(self, packet):
        """
        Compute a packet receveived from the server
        """
        packetID = packet.getVarint()
        if (self.state == PLAY_STATE):
            tab = PLAY_IN
        elif (self.state == LOGIN_STATE):
            tab = LOGIN_IN
        elif (self.state == STATUS_STATE):
            tab = STATUS_IN

        if packetID not in tab:
            Debug("\t%s" % hex(packetID))
        else:    
            name = tab[packetID]['name']
            func = tab[packetID]['func']
            data = tab[packetID]['data']

            if ('trace' in tab[packetID]) and tab[packetID]['trace']:
                Debug(name)
            
            if func != None:
                # decode data
                param = {}
                for i in range(0, len(data), 2):
                    arg = data[i]
                    decode = data[i+1]
                    if '|' not in decode:
                        # no argument needed to decode the parameter
                        val = getattr(packet, 'get'+decode)()
                        param[arg] = val
                    else:
                        # paramater must be added
                        res = decode.split('|')
                        fct = res[0].strip()
                        var = res[1].strip()
                        val = getattr(packet, 'get'+fct)(param[var])
                        param[arg] = val
    
                # call the notification function
                getattr(self, func)(param)


# ------------------------------------------
    def trtDisconnect(self, param):
        Debug("server send a disconnect !!!")

    def trtLoginSuccess(self, param):
        """
        Login accepted
        parameters : 'uuid'    : 'String'
                     'username': 'String'
        """
        #print("Login accepted for '%s', Uuid=%s" % (param['username'], param['uuid']))
        # now change to the PLAY protocol
        self.setStatePlay()
         
    def trtKeepAlive(self, param):
        """
        Reply with a keep alive with the same ID
        """
        Debug(".", end='', flush=True)
        self.Out('keep_alive', keep_alive_id = param['keep_alive_id'])
        
    def trtJoinGame(self, param):
        """ The bot join the game """
        self.players.SetBot(param['entity_id'], self.application.GetBotName())
            
    def trtChat(self, param):
        """
        Print the Chat message
        """
        chat = Chat(param['json_data'])
        txt = chat.GetMessage()
        sender = chat.GetSender()
        self.application.GetCommand().DispatchCommand(txt, sender)
    
    def trtSpawn(self, param):
        """
        Change the Bot position
        """
        Debug("Bot spawned at %d, %d, %d" %(param['x'],param['y'],param['z']))
        self.players.SetBotPosition(param['x'],param['y'],param['z'])
    
    def trtHealth(self, param):
        """
        Update the Health and the Food information
        """
        Debug("Healt = %d, Food = %d" %(param['health'],param['food']))
        self.players.SetBotHealthFood(param['health'], param['food'])

        
    def trtPlayerPositinLook(self, param):
        """
        Update the Bot information regarding its position and orientation
        """
        self.players.SetBotAbsolutePosition(param['x'],param['y'],param['z'])
    
#     def trtPlayerListItem(self, param):
#         """
#         Manage the list of players
#         """
#         self.player.ManageOtherPlayers(param['player_name'], param['online'])
        
    def trtSpawnPlayer(self, param):
        """
        Received when a player becomes visible
        """
        print('Player %s is at %d, %d, %d' % (param['player_name'], param['x'], param['y'], param['z']))
        self.players.AddPlayer(param['entity_id'], param['player_name'])
        self.players.SetPosition(param['entity_id'], param['x']/32, param['y']/32, param['z']/32)
        self.entities.Entity(param['entity_id'])
        self.entities.SetPos(param['entity_id'], param['x']/32, param['y']/32, param['z']/32)
        self.entities.Look(param['entity_id'], param['yaw'], param['pitch'])

# ------------ Entities ------------------------
    def trtEntity(self, id):
        """ Initialisation d'une entité """
        self.entities.Entity(id)
    
    def trtEntityRelativeMove(self, param):
        """ an entity moves """
        self.entities.RelativeMove(param['entity_id'], param['dx']/32, param['dy']/32, param['dz']/32)
        
    def trtEntityLook(self, param):
        """ Entity look information """
        self.entities.Look(param['entity_id'], param['yaw'], param['pitch'])
  
    def trtEntityLookMove(self, param):
        """ Entity change location and look """
        self.entities.RelativeMove(param['entity_id'], param['dx']/32, param['dy']/32, param['dz']/32)
        self.entities.Look(param['entity_id'], param['yaw'], param['pitch'])
        
    def trtEntityTeleport(self, param):
        """ teleport at a fixed location """
        self.entities.SetPos(param['entity_id'], param['x']/32, param['y']/32, param['z']/32)
        self.entities.Look(param['entity_id'], param['yaw'], param['pitch'])
        
    def trtSpawnGlobalEntity(self, param):
        self.entities.SetPos(param['entity_id'], param['x']/32, param['y']/32, param['z']/32)
        self.entities.SetType(param['type'])
