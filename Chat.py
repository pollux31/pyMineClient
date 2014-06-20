'''
Created on 20 juin 2014

@author: Thierry
'''
import json

class Chat(object):
    """
    Manage the Chat exchanges with the server
    This class is focused on Free text chat
    """
    
    def __init__(self, data):
        """
        create the Chat object based on the JSON message
        """
        msg = json.loads(data)
        print (msg)
        
        self.text = ""
        self.type = msg['translate']
        self.sender = msg['with'][0]['text']
        if self.type == 'chat.type.text': 
            self.text = msg['with'][1]
        elif self.type =='commands.message.display.incoming':
            self.text = "".join(msg['with'][1]['extra'])
        
        print("Message from %s : %s" %(self.sender, self.text))
        
        