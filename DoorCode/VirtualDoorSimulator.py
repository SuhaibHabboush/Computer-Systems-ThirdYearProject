#####################################################
#
#	GUI.py
#	Patrick Perron
#
#####################################################

#imports
import sys
import time
import socket
import threading
from tkinter import *
from Door import Door
from widget_virtualdoor import VirtualDoorPanel

class VirtualDoorSimulator(Frame):	
    def __init__(self, master, info):
        Frame.__init__(self, master)
        self.master.wm_title("Phantom Lock - Virtual Door Simulator")
        self.master.iconbitmap(r'images/icon.ico')
        self.master.resizable(False,False)
        self.grid()   

        i=0
        doors = []
        while i<len(info):
            doors.append(VirtualDoorPanel(self, info[i]))
            doors[i].grid(row=0,column=i,sticky=W+E+N+S)
            i+=1