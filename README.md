pyMineClient
============


Tool to create a MineCraft bot client. 
This code uses Python 3.4 version with `asyncio` module to manage Minecraft packets ptotocol.

## Features

* Supports Minecraft 1.7.9 version
* Accepts all packets (even if they are not currently interpreted)
* High level packet interface, with named parameters
* Protocol defined in a description table => easy to change for future versions or evolutions


### Limitation

This version of implementation does not manage authentication and logging. So you must:
* Use the local server (exe or java version) Minecraft_server.1.7.9
* In the server `server.properties` file, change the 'on-line' option to `online-mode=false` 

## Protocol definition

The protocol is described in the `DescProto.py` file. It is split in the 3 main parts listed in the protocol documentation:
* Login
* Play
* Status 

Each part contains 2 tables stored in a Python dictionnary:
* OUT table for the 'Client => Server' packets (Clientbound packets)
* IN table for the 'Server => Clients' packets (Serverbound packets)

### OUT table definition

The goal of this table is to describe the content of packets sent from the Client to the Server. It is based on a python dictionary where the `Key` is the `Packet name` and the `Value` is the packet definition.

The syntax is:
```python 

'packet_name' : [<PacketID>, ['Param1', 'Param1_type', 'Param2', 'Param2_type', ...]]

```

Here after is an example for the Player digging packet (code 0x07)
```python

	'player_digging' : [0x07, ['status', 'Byte',
	                           'x'     , 'Int',
	                           'y'     , 'UByte',
	                           'z'     , 'Int',
	                           'face'  , 'Byte']],
```

Types are defined in the `Packet.py` file. Each type has a getter `getXXXX` to read the data and a setter `toXXXX` to serialize a value, where XXXX is the name of the type used in the packet description.

To send a packet to the server, you just have to call the Out function of the `Protocol` class with the name of the packet and for the parameters list of named arguments.

In the previous example, to send a digging packet, simply call:

```python

protocol.Out('player_digging', status=0, x=213, y=8, z=130, face=3)

```
 The `Out` function will serialize all the data (based on the name and the associated type) and send the packet to the server. 


### OUT table definition

The goal of this table is to describe the content of packets sent by the Server to the Client. It is based on a python dictionary where the `Key` is the `Packet ID` received and the `Value` is the packet definition structure.

The syntax is:
```python 

 <PacketID> :  {
     'name' : '<packet name>’,
     'trace' : True or False,         # if this key is not present, then trace = False
     'func' : '<callback function name>' or None
     'data' : ['param1', 'param1_type', 'param2', 'param2_type', ...]}

```

Here after is an example of the 2 first packets description:
```python

PLAY_IN = {
            0x00 : {'name' : 'keep_alive',
                    'func' : 'trtKeepAlive',
                    'data' : ['keep_alive_id', 'Int']},

            0x01 : {'name' : 'join_game',
                    'trace': True,
                    'func' : None,
                    'data' : ['entity_id' , 'Int',
                              'gamemode'  , 'UByte',
                              'dimension' , 'Byte',
                              'difficulty', 'UByte',
                              'max_player', 'UByte',
                              'level_type', 'String']},
```

#### For the first packet ID 0x00
* The name of the packet is `keep_alive`. This name is printed when the trace is activated. 
* Trace key is not present, so it is like `'trace' : False`
* Function name is `trtKeepAlive`. This function must be declared in the `Protocol` 
* Only one data for this packet: `keep_alive_id` parameter that is an integer 

#### For the packet ID 0x02
The differences are:
* Trace is activated, so the name of this packet will be printed in the console each time it will be received
* The `func` parameter is `None`. In this case the content of the packet will not be analyzed and the `data` part of the packet description is not taken in account. It is listed here only to have the job done in case we want to add a callback function ;-)

#### Callback function definition
When a call back function name is present in a packet definition, a function with the same name must be added in the `Protocol` class.

This function has only one parameter `param` that contains a dictionary with all the data values of the packet. The `key` is the data name and the `value` is the value of this data.

The Keep Alive packet has a callback function `trtKeepAlive` declared, so just add the following function in the `Protocol` class (given for example):

```python

    def trtKeepAlive(self, param):
        """
        Reply with a keep alive containing the same ID
        """
        id = param['keep_alive_id']
        print("for debug, the keep_alive Id received is : %d", id)
        
        # just send the Keep Alive reply with the same ID parameter
        self.Out('keep_alive', keep_alive_id = id)
        
```

#### Special type description
In some cases, the number of data to decode is indicated in the packet. For example, the `destroy entity` packet (code 0x13) has the following data:
* count: length of following array
* Entity IDs: The list of entities of destroy

The problem to decode this packet is that you must know the length of data in order to retrieve the array of entity Ids.
The description of such a packet is:

```python

            0x13 : {'name' : 'destroy_entity',
                    'func' : None,
                    'data' : ['count'     , 'Byte',
                              'entity_ids', 'Intarray|count']},

```
 It uses a specific syntax to declare the type of the array:
` '<standard type>|<data name>'`

* <standard type> is a string corresponding of the data type. Like for other type, the decode function must be declared in the `Packet` class.
* <data name> is the name of a previous parameter. The corresponding value will be given as parameter to the decode function

The corresponding decode function is in this case:

```python

    def toIntarray(self, value):
        """
        return the Int array
        """
        ... 
```
During the call the value parameter will be automatically replaced by the value of the `count` data (a byte in our case).


## Vesrions

### V 0.1 : Initialisation
This version contains the network and packets engine based on packets description file.
Communication with the server is OK and the Minecraft Bot stay alive without server disconnection.

