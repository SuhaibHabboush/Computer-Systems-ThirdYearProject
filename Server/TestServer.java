import java.net.*;
import java.io.*;

public class TestServer extends Thread{
  final int SERVER_PORT = 1400;

  final byte PASS_MSG = 0;
  final byte IMG_MSG = 1;
  final byte D_STAT_MSG = 2;
  final byte LK_MSG = 3;
  //TODO: add the rest of the oppcodes.
  boolean passcodeSuccess;
  boolean imageSendSuccess;
  boolean invalidHomeSuccess;
  boolean invalidDoorSuccess;
  boolean createDoorSuccess;
  boolean unlockDoorRequestRecievedSuccess;
  boolean unlockDoorRequestSentSuccess;
  //NOTE: Maybe have opcode for all doors in house for general requests from webclients to be 0000;
  final String CORECT_PASS = "1324";
  final String INCORECT_PASS = "1234";
  byte[] sendMsg;

  Server server;

  DatagramSocket doorSocket;
  DatagramSocket webclientSocket;
  int SERVER_PORT = 1400;

  public TestServer() {
      this.server = new Server();
      this.webclientSocket = new DatagramSocket();
      this.doorSocket = new DatagramSocket();
      sendMsg = new byte[100];

      server.start();
  }


  public void bulidStandardRequest(byte b, Object o){
    sendMsg[0] = 1;
    sndMsg[1] = ;
    sndMsg[2] = b;
    if (o == null) return;
    else if (o.getType() == String.getType()){
      byte[] tempBytes = o.getBytes();
      int j=0;
      for(int i = 3; i<tempBytes.length; i++){
        sendMsg[i] = tempBytes[j]++;
      }
    }
  }

  public void run(){
    byte[] rcvMsg = new byte[512];
    DatagramPacket recievePacket = new DatagramPacket(rcvMsg, rcvMsg.length);

    System.out.println("Test Server recieve Message to unlock door from webclient");

    buildStandardRequest(PASS_MSG, CORRECT_PASS);
    DataPacket testPacket = new DatagramPacket(sendMsg, sendMsg.length, localHost, SERVER_PORT);

    doorSocket.setSoTimeout(10000);
    doorSocket.send(testPacket);

    doorSocket.recieve(recievePacket);
    for(int i =3)


  }

}
