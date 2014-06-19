'''
Created on 15 juin 2014

@author: Thierry
'''
import struct

class Packet(object):
    
    def __init__(self, buf=None):
        self.data = buf
        self.fct = None
        
#    def callFct(self, function, val):
#        self.fct = function
#        return self.fct(val)
        
    #  Varint
    # -----------------
    def toVarint(self, value):
        """ 
        Converts a number into a varInt bytes array
        """
        result = []   
        while value > 0x7F:
            # only use the lower 7 bits of this byte (big endian)
            # if subsequent length byte, set highest bit to 1, else just insert the value with 
            result.append((value & 0x7F) | 0x80)
            value >>= 7
        result.append(value)
        return result
    
    def getVarintSize(self):
        """
        return the number of byte used to decode the last Varint
        """
        return self.varintSize
        
    
    def getVarint(self):
        """
        Convert the VarInt bytes array to a number.
        Update the buffer
        Update se size used to convert the varint
        """
        self.varintSize = 0
        
        if self.data == None:
            return None
        
        number = 0
        offset = 0
        for curByte in self.data:
            number += (curByte & 0x7F) << offset
            offset += 7
            self.varintSize += 1
            if (curByte & 0x80) == 0:
                break
        
        self.data = self.data[self.varintSize:]  # remove bytes from buffer
        return number
    
    #  String
    # -----------------
    def toString(self, value):
        """
        Converts a string to bytes array
        """
        tmp = bytearray(value, "utf_8")
        buf = self.toVarint(len(value))
        buf.extend(tmp)
        return buf
    
    def getString(self):
        """
        retrun a String from the buffer
        update the buffer
        """
        if self.data == None:
            return None
        packet = Packet(self.data)
        nb = packet.getVarint()
        header = packet.getVarintSize()
        tmp = self.data[header:header+nb]
        self.data = self.data[nb+header:] # remove bytes from buffer
        return tmp
        
    
    #  Bool
    # -----------------
    def toBool(self, value):
        """
        Converts a boolean to 1 byte
        """
        return struct.pack(">?", value)
    
    def getBool(self):
        """
        retrun the boolean
        update the buffer used
        """
        if self.data == None:
            return None
        tmp = struct.unpack_from(">?", self.data)
        self.data = self.data[1:] # remove bytes from buffer
        return tmp[0]
    
    
    #  Byte
    # -----------------
    def toByte(self, value):
        """
        Converts a value to 1 byte
        """
        return struct.pack(">b", value)
    
    def getByte(self):
        """
        retrun the byte
        update the buffer used
        """
        if self.data == None:
            return None
        tmp = struct.unpack_from(">b", self.data)
        self.data = self.data[1:] # remove bytes from buffer
        return tmp[0]
    
    
    #  Unsigned Byte
    # -----------------
    def toUByte(self, value):
        """
        Converts a value to 1 byte
        """
        return struct.pack(">B", value)
    
    def getUByte(self):
        """
        retrun the byte
        update the buffer used
        """
        if self.data == None:
            return None
        tmp = struct.unpack_from(">B", self.data)
        self.data = self.data[1:] # remove bytes from buffer
        return tmp[0]
    
    
    #  Unsigned Short
    # -----------------
    def toUShort(self, value):
        """
        Converts an Unsigned Short to 2 bytes
        """
        return struct.pack(">H", value)
    
    def getUShort(self):
        """
        retrun the unsigned short
        update the buffer used
        """
        if self.data == None:
            return None
        
        tmp = struct.unpack_from(">H", self.data)        
        self.data = self.data[2:] # remove bytes from buffer
        return tmp[0]
    
    
    #  Short
    # -----------------
    def toShort(self, value):
        """
        Converts an Short to 2 bytes
        """
        return struct.pack(">h", value)
    
    def getShort(self):
        """
        retrun the short 
        update the buffer used
        """
        if self.data == None:
            return None
        tmp = struct.unpack_from(">h", self.data)
        self.data = self.data[2:] # remove bytes from buffer
        return tmp[0]
    
    
    #  Int
    # -----------------
    def toInt(self, value):
        """
        Converts an Integer to 4 bytes
        """
        return struct.pack(">i", value)
    
    def getInt(self):
        """
        retrun the Integer 
        update the buffer used
        """
        if self.data == None:
            return None
        tmp = struct.unpack_from(">i", self.data)
        self.data = self.data[4:] # remove bytes from buffer
        return tmp[0]
    

    #  Long
    # -----------------
    def toLong(self, value):
        """
        Converts an Long to 8 bytes
        """
        return struct.pack(">q", value)
    
    def getLong(self):
        """
        retrun the Long 
        update the buffer used
        """
        if self.data == None:
            return None
        tmp = struct.unpack_from(">q", self.data)
        self.data = self.data[8:] # remove bytes from buffer
        return tmp[0]
    

    #  Float
    # -----------------
    def toFloat(self, value):
        """
        Converts an Integer to 4 bytes
        """
        return struct.pack(">f", value)
    
    def getFloat(self):
        """
        retrun the Integer 
        update the buffer used
        """
        if self.data == None:
            return None
        tmp = struct.unpack_from(">f", self.data)
        self.data = self.data[4:] # remove bytes from buffer
        return tmp[0]
    

    #  Double
    # -----------------
    def toDouble(self, value):
        """
        Converts an Double to 8 bytes
        """
        return struct.pack(">d", value)
    
    def getDouble(self):
        """
        retrun the Integer 
        update the buffer used
        """
        if self.data == None:
            return None
        tmp = struct.unpack_from(">d", self.data)
        self.data = self.data[8:] # remove bytes from buffer
        return tmp[0]
    

    #  Byte array
    # -----------------
    def toBytearray(self, value):
        """
        return the bytes array
        """
        return value
    
    def getBytearray(self, len):
        """
        retrun the bytes array 
        update the buffer
        """
        if self.data == None:
            return None
        
        tmp = self.data[0:len]
        self.data = self.data[2:]  # remove bytes from buffer
        return tmp
   
    
    #  Int array
    # -----------------
    def toIntarray(self, value):
        """
        return the Int array
        """
        tmp = []
        offset = 0
        for val in value:
            struct.pack_into(">i", tmp, offset, val)
            offset += 2
        return value
    
    def getIntarray(self, len):
        """
        retrun the Int array 
        update the buffer
        """
        if self.data == None:
            return None
        
        offset = 0
        tmp = []
        for i in range(len):
            tmp.append(struct.unpack_from(">i", self.data, offset))
            offset += 2
        self.data = self.data[2*len:]  # remove bytes from buffer
        return tmp
    

    #  Slot
    # -----------------
    def getSlot(self):
        """
        return a dictionnary corresponding to the Slot data
        update the buffer
        """
        tmp={}
        tmp['block_id'] = self.getShort()
        if tmp['block_id'] != -1:
            tmp['item_count'] = self.getByte()
            tmp['item_damage'] = self.getShort()
            tmp['length'] = self.getShort()
            if tmp['length'] != -1:
                tmp['data'] = self.getBytearray(tmp['length'])
        return tmp        
    
    #  Metadata
    # -----------------
    def getMetadata(self):
        """
        retrun a dictionay corresponding to the Metadata 
        update the buffer
        """
        if self.data == None:
            return None
        
        tmp = {}
        while True:
            item = self.getByte()
            if item == 127:
                break
            index = item & 0x1F
            type = item >> 5
            
            if type == 0 :
                tmp[index] = self.getByte()
            elif type == 1:
                tmp[index] = self.getShort()
            elif type == 2:
                tmp[index] = self.getInt()
            elif type == 3:
                tmp[index] = self.getFloat()
            elif type == 4:
                tmp[index] = self.getString()
            elif type == 5:
                tmp[index] = self.getSlot()
            elif type == 6:
                tmp[index] = {'x':self.getInt(), 'y':self.getInt(), 'z':self.getInt()}
        return tmp
            
        tmp = self.data[0:len]
        self.data = self.data[2:]  # remove bytes from buffer
        return tmp

    #  PropertyArray
    # -----------------
    def PropertyArray(self, count):
        """
        retrun an array of Entity Properties. Each value is an dictionnary containing the Property
        update the buffer
        """
        tmp = []
        for i in range(count):
            prop = {}
            prop['key'] = self.getString()
            prop['value'] = self.getDouble()
            prop['length'] = self.getShort()
            mod = []
            for j in range(prop['length']):
                item = {}
                item['uuid'] = self.get128bitsInteger()
                item['amount'] = self.getDouble()
                item['operation'] = self.getByte()
                mod.appen(item)
            tmp.append(prop)
                
            
    def get128bitsInteger(self):
        tmp = struct.unpack_from(">qq", self.data)[0]      
        self.data = self.data[16:] # remove bytes from buffer
        return (tmp[0] << 64) + tmp[1]


