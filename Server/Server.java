import java.io.*;
import java.net.*;
import java.util.ArrayList;

public class Server extends Thread{
  private String passcode = "1472";
  private DatagramSocket receiveSocket;
  private ArrayList<Thread> activeRequests;

  private static final int PORT_NUMBER = 1400;

  /*
  * Creates new server Thread initalizes reveive socket and active requests
  */
  public Server(){
      activeRequests = new ArrayList<Thread>();
      try{
        receiveSocket = new DatagramSocket(PORT_NUMBER);
      } catch (SocketException e){
        e.printStackTrace();
      }
  }

  public void recieveAndControl(){
    byte[] msg = new byte[100];
    DatagramPacket receivePacket = new DatagramPacket(msg, msg.length);

    while(true){
        System.out.println("Server waiting..\n");
        try {
          receiveSocket.receive(receivePacket);
        } catch(IOException e){
          e.printStackTrace();
        }
        System.out.println("Request Received");
        addActiveRequest(new ControlThread(receivePacket));
    }
  }
  public void addActiveRequest(Thread request){
    activeRequests.add(request);
    request.start();
  }
  public String getPasscode(){
    return passcode;
  }

}
