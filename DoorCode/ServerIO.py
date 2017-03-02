#===============================================================
# ServerIO.py
#---------------------------------------------------------------
# Collection of IO functions for a door connecting to server
#===============================================================
#imports
import time
import socket
#===============================================================
class ServerIO():
#===============================================================
    #===============================================================
    # Initializing Code
    #---------------------------------------------------------------
    def __init__(self, homeID, doorID):        # Initialize servers and ports
        self.HOME_ID = int(homeID)
        self.DOOR_ID = int(doorID)
        # Where to Send
        self.SERVER_ADDRESS = '127.0.0.1'
        self.SERVER_PORT    = 1400
        # Where to Receive
        self.DOOR_ADDRESS   = '127.0.0.1'
        self.DOOR_PORT      = 1400+10*int(homeID)+int(doorID)

        self.SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.RECEIVE = (self.DOOR_ADDRESS, self.DOOR_PORT)
        self.SOCKET.bind(self.RECEIVE)
        

    def sendPassword(self, password):
        toSend = bytes([
            self.HOME_ID&0xFF, 
            self.DOOR_ID&0xFF, 
            0x00, # Opcode for sending message 
            (ord(password[0]))&0xFF, 
            (ord(password[1]))&0xFF, 
            (ord(password[2]))&0xFF,
            (ord(password[3]))&0xFF
        ])
        self.send(toSend)

    def sendPicture(self, picture):
        i=1
        #self.send(picture)

    def sendState(self, state):
        if state is True:
            toSend = bytes([ 
                self.HOME_ID&0xFF, 
                self.DOOR_ID&0xFF,
                0x03, 
                0x00 
            ])
        else: 
             toSend = bytes([ 
                self.HOME_ID&0xFF, 
                self.DOOR_ID&0xFF,
                0x03, 
                0xFF 
            ])
        self.send(toSend)           

    def send(self, message):
        self.SOCKET.sendto(message, (self.SERVER_ADDRESS, self.SERVER_PORT))

    def receive(self):
        buff, address = self.SOCKET.recvfrom(self.DOOR_PORT);
        return buff