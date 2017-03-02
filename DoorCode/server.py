# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(1400)
server_address = ('localhost', port)
s.bind(server_address)

while True:

    print ("Waiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop " % port)

    buf, address = s.recvfrom(port)

    # Reveive Message
    HomeID = int(buf[0])
    DoorID = int(buf[1])
    opcode = buf[2]

    # Password Request:
    if opcode == 0x00:
        response = None
        password = buf[3:].decode()
        print(str(HomeID)+" "+str(DoorID)+" "+str(opcode)+" "+password)
        if HomeID == 0:
            if password == "1230": response = bytes([ 0x00 , 0x00])
            else: response = bytes([ 0x00 , 0xFF])
        elif HomeID == 1:
            if password == "1231": response = bytes([ 0x00 , 0x00])
            else: response = bytes([ 0x00 , 0xFF])
        elif HomeID == 2:
            if password == "1232": response = bytes([ 0x00 , 0x00])
            else: response = bytes([ 0x00 , 0xFF])
        elif HomeID == 3:
            if password == "1233": response = bytes([ 0x00 , 0x00])
            else: response = bytes([ 0x00 , 0xFF])
        elif HomeID == 4:
            if password == "1234": response = bytes([ 0x00 , 0x00])
            else: response = bytes([ 0x00 , 0xFF])
        elif HomeID == 5:
            if password == "1235": response = bytes([ 0x00 , 0x00])
            else: response = bytes([ 0x00 , 0xFF])
        elif HomeID == 6:
            if password == "1236": response = bytes([ 0x00 , 0x00])
            else: response = bytes([ 0x00 , 0xFF])
        else:
            print("K")
            exit(1)
            response = bytes([ 0xFF ])
        s.sendto(response, ('localhost', 1400+int(HomeID)*10+int(DoorID)))
    elif opcode == 0x05:
        print(str(HomeID)+" "+str(DoorID))
        if 0 <= HomeID <= 100 and 0 <= DoorID <= 100:
            response = ((str(0x05)+str(0x00)+'Front;Patrick Perron, Patty Perron;1234').encode('utf-8'))
            print(str(response.decode("utf-8")))
            print(str(response))
        else:
            response =((str(0x05)+str(0xFF)).encode('utf-8'))
        s.sendto(response, ('localhost', 1400+int(HomeID)*10+int(DoorID)))

    elif opcode == 0x03:
        state = buf[3]
        if state == 0x00:
            print("("+str(HomeID)+","+str(DoorID)+") Door in SECURED state")
        else:
            print("("+str(HomeID)+","+str(DoorID)+") Door in UNSECURED state")

    else:
        print("L")
        exit(1)
        response = bytes([ 0xFF ])

    

s.shutdown(1)
