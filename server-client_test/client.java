import java.io.*;
import java.net.*;

class client {
	static  DataInputStream in = null;
	static  DataOutputStream out = null;

	public static void main(String[] args) throws IOException {
		System.out.println("Connecting to... ");

		createSocket("localhost", 8080);

		sendMess(in, out);
	}

	private static void createSocket(String server, int port){ 
		
		try {
			Socket socket = new Socket(server, port);

			InputStream sin = socket.getInputStream();
			OutputStream sout = socket.getOutputStream();

			in = new DataInputStream(sin);
			out = new DataOutputStream(sout);

		} catch (Exception e) {
			e.printStackTrace();
		}

		System.out.println("client is connected to server");
	}

	private static void sendMess(DataInputStream in, DataOutputStream out){
		try{
			String mess = createMess();
			out.writeUTF(mess);
			out.flush();
			mess= in.readUTF();
			System.out.println("You say "+mess+ " to server");	

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	private static String createMess(){ 
		return "hello, server, whatsapp??";
	}
}