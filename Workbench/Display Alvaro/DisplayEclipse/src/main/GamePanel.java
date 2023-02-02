package main;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;

import javax.swing.JPanel;
import javax.swing.ImageIcon;


public class GamePanel extends JPanel implements Runnable{
	final int ogTileSize = 32;
	final int scale = 3;
	final int tileSize = ogTileSize * scale;
	final int maxScreenCol = 13;
	final int maxScreenRow = 4;
	
	Thread gameThread;
	
	final int screenWidth = tileSize * maxScreenCol;
	final int screenHeight = tileSize * maxScreenRow;
	
	Image logo = new ImageIcon("C:\\ISC GitHub\\ISC_logo_transparent.jpg").getImage();

	
	public GamePanel()
	{
		this.setPreferredSize(new Dimension(screenWidth, screenHeight));
		this.setBackground(Color.darkGray);
		this.setDoubleBuffered(true);
	}
	
	public void startGameThread() 
	{
		gameThread = new Thread(this);
		gameThread.start();
	}

	@Override
	public void run()
	{
		while(gameThread != null)
		{
			//System.out.println("the thread is working");
			// 1. Update
			update();
			
			
			//2. Draw
			repaint();
		}
	}
	
	public void update()
	{
		
	}
	
	public void paintComponent(Graphics g)
	{
			super.paintComponent(g); 		// super se refiere a la clase padre de GamePanel
									 		// que es JPanel.
		Graphics2D g2 = (Graphics2D)g;
		
		g2.drawImage(logo, 6, 7, 245, 106, this);		// ESTO NO SE TOCA ES EL LOGO
		
		// bloques de info
		g2.setColor(Color.orange);			// accumulator temps
		g2.drawRoundRect(265, 7, 195, 91, 10, 10);
		
		g2.setColor(Color.green);			// delta
		g2.drawRoundRect(465, 7, 311, 91, 10, 10);
		
		g2.setColor(Color.orange);			// engine temps
		g2.drawRoundRect(781, 7, 195, 91, 10, 10);
		
		g2.setColor(Color.magenta);			// left temps
		g2.drawRoundRect(265, 103, 195, 212, 10, 10);
		
		g2.setColor(Color.white);			// speed
		g2.drawRoundRect(465, 103, 311, 212, 10, 10);
		
		g2.setColor(Color.magenta);			// right temps
		g2.drawRoundRect(781, 103, 195, 212, 10, 10);
		
		g2.setColor(Color.yellow);				// SoC
		g2.drawRoundRect(265, 320, 712, 60, 10, 10);
	}
}
