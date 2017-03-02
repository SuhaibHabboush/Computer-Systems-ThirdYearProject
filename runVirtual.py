#####################################################
#
#	runVirtual.py
#	Patrick Perron
#
#####################################################

#imports
from tkinter import *
from VirtualDoorManager import VirtualDoorManager
from VirtualDoorSimulator import VirtualDoorSimulator


def main():
    root1 = Tk()
    door = VirtualDoorManager(master=root1)
    door.mainloop()
    root1.destroy()
    if len(door.output) > 0:
        root2 = Tk()
        door = VirtualDoorSimulator(master=root2, info=door.output)
        door.mainloop()
        root2.destroy()

main()

#####################################################
