#####################################################
#
#	GUI.py
#	Patrick Perron
#
#####################################################

#imports
import threading
from tkinter import *
from Door import Door
from widget_keypad    import KeypadPanel
from widget_doorpanel import DoorPanel
from widget_lockpanel import LockPanel
from widget_infopanel import InfoPanel

class VirtualDoorPanel(Frame):	
    def __init__(self, master, info):
        Frame.__init__(self, master)

        self["relief"] = "raised"
        self["borderwidth"] = "2"
        self.DOOR = Door(info[0], info[1])
        # Run Door Thread in background
        door_thread = threading.Thread(target=self.DOOR.runVirtual,args=())
        door_thread.daemon = True
        door_thread.start()

        self.grid()   
        # Info Panel
        self.infoPanel = InfoPanel(self, self.DOOR)
        self.infoPanel.grid(row=0,column=0,sticky=W+E+N+S)
        # Door Panel
        self.doorpanel = DoorPanel(self, self.DOOR)
        self.doorpanel.grid(row=1,column=0,sticky=W+E+N+S)
        # Lock Panel
        self.lockPanel = LockPanel(self,self.DOOR)
        self.lockPanel.grid(row=2,column=0,sticky=W+E+N+S)
        # Keypad Panle
        self.keypadPanel = KeypadPanel(self, self.DOOR)
        self.keypadPanel.grid(row=3,column=0,sticky=W+E+N+S)

