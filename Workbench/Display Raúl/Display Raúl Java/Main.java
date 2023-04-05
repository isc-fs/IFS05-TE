import java.awt.*;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.GraphicsDevice;
import java.awt.GraphicsEnvironment;

public class Main {
	public static void main(String argv[]) {
	
		JFrame window = new JFrame();
		window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
        GraphicsDevice[] devices = ge.getScreenDevices();
        GraphicsDevice device = devices[0];
		device.setFullScreenWindow(window); 	

		window.setResizable(false);
		window.setTitle("Display");
		
		
		
		GamePanel gamePanel = new GamePanel();
		window.add(gamePanel);
		
		window.pack();
		
		gamePanel.startGameThread();
		
		window.setLocationRelativeTo(null);
		window.setVisible(true);
	}
}
