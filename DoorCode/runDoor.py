# Simple Program to Run a Door on a preset RPI

# imports
import sys
from Door import Door

# Check if Input is Valid
if len(sys.argv) is not 3:
	print("Error: Must pass with Valid HomeID and DoorID"); exit(1)
if int(sys.argv[1]) < 0 or 255 < int(sys.argv[1]):
	print("Error: HomeID must be between 0 and 255"); exit(1)
if int(sys.argv[2]) < 0 or 255 < int(sys.argv[2]):
	print("Error: DoorID must be between 0 and 255"); exit(1)

#Run Door
HomeID = sys.argv[1]
DoorID = sys.argv[2]

print("Connecting to Door: HomeID("+HomeID+"), DoorID("+DoorID+")")

door = Door(HomeID, DoorID)
door.runVirtual()

