#####################################################
#
#	GUI.py
#	Patrick Perron
#
#####################################################

#imports
from tkinter import *
from Door import Door

	
class InfoPanel(Frame):
    def __init__(self, master, door):
        Frame.__init__(self, master)
        self.grid()
		# Door ID
        self.DoorIDTag = Label(self)
        self.DoorIDTag.config(font=("Helvetica", 7))
        self.DoorIDTag["text"]   = "Door ID"
        self.DoorIDTag["anchor"] = "e"
        self.DoorIDTag["width"]  = "7"
        self.DoorIDTag["bg"] = "white"
        self.DoorIDTag["fg"] = "black"
        self.DoorIDTag["relief"] = "flat"
        self.DoorIDTag.grid(row=1,column=0,sticky=W+E+N+S)
        self.DoorIDLabel = Label(self)
        self.DoorIDLabel["text"]  = str(door.DOOR_ID)
        self.DoorIDLabel["anchor"] = "w"
        self.DoorIDLabel["width"] = "12"
        self.DoorIDLabel["bg"] = "white"
        self.DoorIDLabel["fg"] = "black"
        self.DoorIDLabel["relief"] = "sunken"
        self.DoorIDLabel.grid(row=1,column=1,sticky=W+E+N+S)
		# Home ID
        self.HomeIDTag = Label(self)
        self.HomeIDTag.config(font=("Helvetica", 7))
        self.HomeIDTag["text"] = "Home ID"
        self.HomeIDTag["anchor"] = "e"
        self.HomeIDTag["width"] = "7"
        self.HomeIDTag["bg"] = "white"
        self.HomeIDTag["fg"] = "black"
        self.HomeIDTag["relief"] = "flat"
        self.HomeIDTag.grid(row=0,column=0,sticky=W+E+N+S)
        self.HomeIDLabel = Label(self)
        self.HomeIDLabel["text"]  = str(door.HOME_ID)
        self.HomeIDLabel["anchor"] = "w"
        self.HomeIDLabel["width"] = "12"
        self.HomeIDLabel["bg"] = "white"
        self.HomeIDLabel["fg"] = "black"
        self.HomeIDLabel["relief"] = "sunken"
        self.HomeIDLabel.grid(row=0,column=1,sticky=W+E+N+S)
		# Door Owner
        self.OwnerTag = Label(self)
        self.OwnerTag.config(font=("Helvetica", 7))
        self.OwnerTag["text"] = "Owner"
        self.OwnerTag["anchor"] = "e"
        self.OwnerTag["width"] = "7"
        self.OwnerTag["bg"] = "white"
        self.OwnerTag["fg"] = "black"
        self.OwnerTag["relief"] = "flat"
        self.OwnerTag.grid(row=2,column=0,sticky=W+E+N+S)
        self.OwnerLabel = Label(self)
        self.OwnerLabel["text"]  = "PPerron"
        self.OwnerLabel["anchor"] = "w"
        self.OwnerLabel["width"] = "12"
        self.OwnerLabel["bg"] = "white"
        self.OwnerLabel["fg"] = "black"
        self.OwnerLabel["relief"] = "sunken"
        self.OwnerLabel.grid(row=2,column=1,sticky=W+E+N+S)
		# Door Code
        self.CodeTag = Label(self)
        self.CodeTag.config(font=("Helvetica", 7))
        self.CodeTag["text"] = "Password"
        self.CodeTag["anchor"] = "e"
        self.CodeTag["width"] = "7"
        self.CodeTag["bg"] = "white"
        self.CodeTag["fg"] = "black"
        self.CodeTag["relief"] = "flat"
        self.CodeTag.grid(row=3,column=0,sticky=W+E+N+S)
        self.CodeLabel = Label(self)
        self.CodeLabel["text"]  = "123456"
        self.CodeLabel["anchor"] = "w"
        self.CodeLabel["width"] = "12"
        self.CodeLabel["bg"] = "white"
        self.CodeLabel["fg"] = "black"
        self.CodeLabel["relief"] = "sunken"
        self.CodeLabel.grid(row=3,column=1,sticky=W+E+N+S)
		
