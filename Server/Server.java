import java.io.*;
import java.net.*;
import java.util.ArrayList;

public class Server extends Thread{

  private DatagramSocket receiveSocket;
  private ArrayList<Thread> activeRequests;

  private static final int PORT_NUMBER = 1400;

  /*
  * Creates new server Thread initalizes reveive socket and active requests
  */
  public Server(){
      activeRequests = new ArrayList<Thread>();
      try{
        recieveSocket = new DatagramSocket(PORT_NUMBER);
      } catch (SocketException e){
        e.printStackTrace();
      }
  }

  public void recieveAndControl(){
    

  }


}
