package main;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.Font;

import javax.swing.JPanel;
import javax.swing.JLabel;
import javax.swing.ImageIcon;

public class GamePanel extends JPanel implements Runnable{
	final int ogTileSize = 32;
	final int scale = 3;
	final int tileSize = ogTileSize * scale;
	final int maxScreenCol = 13;
	final int maxScreenRow = 4;
	
	Thread gameThread;
	
	Color fondo = new Color(25, 26, 30);
	Color ISC = new Color(251, 187, 28);
	Color ISCgreen = new Color(92, 132, 28);
	
	Font font = new Font("Helvetica SemiBold", Font.BOLD, 120);
	Font font2 = new Font("Helvetica SemiBold", Font.BOLD, 57);

	
	final int screenWidth = tileSize * maxScreenCol;
	final int screenHeight = tileSize * maxScreenRow;
	
	Image logo = new ImageIcon("C:\\ISC GitHub\\ISC_logo_transparent.jpg").getImage();

	
	public GamePanel()
	{
		this.setPreferredSize(new Dimension(screenWidth, screenHeight));
		this.setBackground(fondo);
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
		
		g2.setFont(font);
		
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
		g2.drawRoundRect(270, 108, 185, 99, 10, 10);		//FL
		g2.drawRoundRect(270, 212, 185, 99, 10, 10);		//RL

		g2.setColor(ISC);					// speed
		g2.drawRoundRect(465, 103, 311, 212, 10, 10);
		g2.setColor(Color.white);
	    g2.drawString("80", 554, 247);
		
		g2.setColor(Color.magenta);			// right temps
		g2.drawRoundRect(781, 103, 195, 212, 10, 10);
		g2.drawRoundRect(786, 108, 185, 99, 10, 10);		//FR
		g2.drawRoundRect(786, 212, 185, 99, 10, 10);		//RR
		
		g2.setColor(ISC);					// SoC
		g2.drawRoundRect(265, 320, 712, 60, 10, 10);
		g2.fillRoundRect(265, 320, 450, 60, 10, 10);
	    g2.setColor(Color.white);
		g2.setFont(font2);
	    g2.drawString("60%", 590, 370);	    	    
	}
}
