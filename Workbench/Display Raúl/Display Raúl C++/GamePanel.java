import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.Font;
import java.awt.FontMetrics;

import javax.swing.JPanel;
import javax.swing.JLabel;
import javax.swing.ImageIcon;

import java.io.*;
import java.lang.Thread;


public class GamePanel extends JPanel implements Runnable{
	Thread gameThread;

	private boolean showRectangle = true;
	static boolean visible = true;
	
	Color fondo = new Color(25, 26, 30);
	Color ISC = new Color(251, 187, 28);
	Color ISCgreen = new Color(92, 132, 28);
	
	Font font = new Font("Helvetica SemiBold", Font.BOLD, 40); //speed
	Font font2 = new Font("Helvetica SemiBold", Font.BOLD, 57); //SoC
	Font font3 = new Font("Helvetica SemiBold", Font.BOLD, 13); //batteries, tyres, inversor, engine
	Font font4 = new Font("Helvetica SemiBold", Font.BOLD, 30); //throttle, brake
		
	public GamePanel()
	{
		this.setPreferredSize(new Dimension(1280, 400));//screenWidth, screenHeight
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
			// 1. Update
			update();
	
			//2. Draw
			repaint();
		}
	}
	
	public void update()
	{
		// temporizador para cambiar el valor de la variable showRectangle
		try {
			Thread.sleep(500);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
		showRectangle = !showRectangle; // alterna el valor de la variable booleana entre true y false
		
	}
	
	public void paintComponent(Graphics g)
	{
			super.paintComponent(g); 		
									 		
		Graphics2D g2 = (Graphics2D)g;

// warnings
		if (visible && showRectangle) {
			g2.setColor(Color.red);
			int x1 = 40;
			int y1 = 103;
			g2.fillRoundRect(x1, y1, 185, 212, 10, 10);
			g2.drawRoundRect(30, 93, 205, 232, 10, 10);
			g2.setColor(Color.white);
			g2.setFont(font4);	
			FontMetrics fm1 = g.getFontMetrics(); 
			int textWidth1 = fm1.stringWidth("WARNING");
			int textHeight1 = fm1.getHeight();
			int x_text1 = (185 - textWidth1) / 2 + x1; 
			int y_text1 = (212 - textHeight1) / 2 + fm1.getAscent() + y1;
			g2.drawString("WARNING", x_text1, y_text1);
		}
		
		// drawRoundRect​(int x, int y, int width, int height, int arcWidth, int arcHeight)
// inversor
		g2.setColor(Color.orange);			
		int x = 265;
		int y = 7; 
		g2.drawRoundRect(x, y, 195, 91, 10, 10);	
		g2.setFont(font3);
		FontMetrics fm = g.getFontMetrics(); 
    	int textWidth = fm.stringWidth("INVERSOR");
    	int textHeight = fm.getHeight();
    	int x_text = (195 - textWidth) / 2 + x; 
    	int y_text = (91 - textHeight) / 2 + fm.getAscent() + y;
	    g2.drawString("INVERSOR", x_text, y+20);	  

// batteries
		g2.setColor(Color.green);			
		x = 465;
		y = 7; 
		g2.drawRoundRect(x, y, 311, 91, 10, 10);	
		g2.setFont(font3);	
    	textWidth = fm.stringWidth("BATTERIES");
    	textHeight = fm.getHeight();
    	x_text = (311 - textWidth) / 2 + x; 
    	y_text = (91 - textHeight) / 2 + fm.getAscent() + y;
	    g2.drawString("BATTERIES", x_text, y+20);
	
// engine 
		g2.setColor(Color.orange);			
		x = 781;
		y = 7; 
		g2.drawRoundRect(x, y, 195, 91, 10, 10);	
		g2.setFont(font3);
    	textWidth = fm.stringWidth("ENGINE");
    	textHeight = fm.getHeight();
    	x_text = (195 - textWidth) / 2 + x; 
    	y_text = (91 - textHeight) / 2 + fm.getAscent() + y;
	    g2.drawString("ENGINE", x_text, y+20);	
		
// left tyres
		g2.setColor(Color.magenta);			
		g2.drawRoundRect(265, 103, 195, 212, 10, 10);
		x = 270;
		y = 108; 
		g2.drawRoundRect(x, y, 185, 99, 10, 10);		//FL		
		g2.setFont(font3);
    	textWidth = fm.stringWidth("FL");
    	textHeight = fm.getHeight();
    	x_text = (185 - textWidth) / 2 + x; 
    	y_text = (99 - textHeight) / 2 + fm.getAscent() + y;
	    g2.drawString("FL", x_text, y+20);	
		y = 212; 
		g2.drawRoundRect(x, y, 185, 99, 10, 10);		//RL
    	textWidth = fm.stringWidth("RR");
    	textHeight = fm.getHeight();
    	x_text = (185 - textWidth) / 2 + x; 
    	y_text = (99 - textHeight) / 2 + fm.getAscent() + y;
	    g2.drawString("RR", x_text, y+20);

// speed
		g2.setColor(ISC);					
		g2.setFont(font);
		FontMetrics fm2 = g.getFontMetrics();
		x = 465;
		y = 103; 
		g2.drawRoundRect(x, y, 311, 212, 10, 10);
    	textWidth = fm2.stringWidth("SPEED"); 
    	textHeight = fm2.getHeight();
    	x_text = (311 - textWidth) / 2 + x; 
    	y_text = (212 - textHeight) / 2 + fm2.getAscent() + y;
	    g2.drawString("SPEED", x_text, y+40);	

// right tyres	
		g2.setColor(Color.magenta);			
		g2.drawRoundRect(781, 103, 195, 212, 10, 10);
		x = 786;
		y = 108; 
		g2.drawRoundRect(x, y, 185, 99, 10, 10);		//FR	
		g2.setFont(font3);
    	textWidth = fm.stringWidth("FR");
    	textHeight = fm.getHeight();
    	x_text = (185 - textWidth) / 2 + x; 
    	y_text = (99 - textHeight) / 2 + fm.getAscent() + y;
	    g2.drawString("FR", x_text, y+20);	
		y = 212; 
		g2.drawRoundRect(x, y, 185, 99, 10, 10);		//RR
    	textWidth = fm.stringWidth("RR");
    	textHeight = fm.getHeight();
    	x_text = (185 - textWidth) / 2 + x; 
    	y_text = (99 - textHeight) / 2 + fm.getAscent() + y;
	    g2.drawString("RR", x_text, y+20);

// SoC
		g2.setColor(ISC);					
		g2.drawRoundRect(265, 320, 712, 60, 10, 10);
		g2.fillRoundRect(265, 320, 450, 60, 10, 10);
	    g2.setColor(Color.white);
		g2.setFont(font2);
	    g2.drawString("60%", 590, 370);	   

// brake
		g2.setColor(Color.red);			
		g2.drawRoundRect(1050, 40, 60, 320, 10, 10);
		g2.fillRoundRect(1050, 264, 60, 96, 10, 10);
	    g2.setColor(Color.white);
		g2.setFont(font4);
	    g2.drawString("30%", 1050, 200);	

// throttle
		g2.setColor(Color.green);			
		g2.drawRoundRect(1150, 40, 60, 320, 10, 10);
		g2.fillRoundRect(1150, 137, 60, 224, 10, 10);
	    g2.setColor(Color.white);
		g2.setFont(font4);
	    g2.drawString("70%", 1150, 200);	

	}
}

