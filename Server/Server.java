import java.io.*;
import java.net.*;
import java.util.ArrayList;

public class Server extends Thread{
  private String passcode = "1324";
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

  public void run(){
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


  private class ControlThread extends Thread {
    private DatagramPacket responsePacket;
    private DatagramPacket packet;
  	protected boolean doorStatus;
  	protected boolean keypadRequest;
  	protected boolean imageRequest;
  	protected boolean lockDoorRequest;
    final byte PASS_MSG = 0;
    final byte IMG_MSG = 1;
    final byte D_STAT_MSG = 2;
    final byte LK_MSG = 3;
  	public ControlThread (DatagramPacket packet)
  	{
  		this.packet=packet;
  		doorStatus = false;
  		keypadRequest = false;
  		imageRequest = false;
  		lockDoorRequest = false;
  	}

  	public void run() {
  		byte[] msg = packet.getData();
      //TODO:Check the first two bits to decide the type where is msg is comign from
  		//house number and door number.
  		if (msg[2] == PASS_MSG) {
        keypadRequest(msg);
  		}else if (msg[2] == IMG_MSG) {
        imageRequest(msg);
  		}else if (msg[2] == D_STAT_MSG){
        doorStateMessage(msg);
  		}else if (msg[2] == LK_MSG){
        lockDoorMessage(msg);
      }
    }

    private void keypadRequest(byte[] msg){
      byte[] pascode = new byte[97];
      int j=0;
      for(int i=3; i<msg.length; i++){
        passcode[j++] = msg[i];
      }
      if(Arrays.toString(passcode).equals(Server.getPasscode())){
        buildResponse(UNLOCK);
      }
    }
    private void imageRequest(byte[] msg){
      return;
    }
    private void doorStateMessage(byte[] msg){
      return;
    }
    private void lockDoorMessage(byte[] msg){
      return;
    }
    private void buildResponse(byte key, byte[] msg){
      //TODO: make responseMsg out of first three bytes of the recievePacket along with unlock key
      byte[] responseMsg;

      responsePacket = new DatagramPacket(responseMsg, responseMsg.length, recievePacket.getAddress(), recievePacket.getPort());
    }

  }
}
