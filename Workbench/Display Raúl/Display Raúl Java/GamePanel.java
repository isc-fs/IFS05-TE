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
		this.setPreferredSize(new Dimension(1920, 480));//screenWidth, screenHeight
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
			int x1 = 60;
			int y1 = 103;
			g2.fillRoundRect(x1, y1, 185, 212, 10, 10);
			g2.drawRoundRect(x1-10, 93, 205, 232, 10, 10);
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
		int x = 399;
		int y = 10;
		int width = 293;
		int height = 109;
		g2.drawRoundRect(x, y, width, height, 10, 10);	
		g2.setFont(font3);
		FontMetrics fm = g.getFontMetrics(); 
    	int textWidth = fm.stringWidth("INVERSOR");
    	int textHeight = fm.getHeight();
    	int x_text = (width - textWidth) / 2 + x; 
    	int y_text = (height - textHeight) / 2 + fm.getAscent() + y;
	    g2.drawString("INVERSOR", x_text, y+20);	  

// batteries
		g2.setColor(Color.green);			
		x = 698;
		y = 10; 
		width = 467;
		height = 109;
		g2.drawRoundRect(x, y, width, height, 10, 10);	
		g2.setFont(font3);	
    	textWidth = fm.stringWidth("BATTERIES");
    	textHeight = fm.getHeight();
    	x_text = (width - textWidth) / 2 + x; 
    	y_text = (height - textHeight) / 2 + fm.getAscent() + y;
	    g2.drawString("BATTERIES", x_text, y+20);
	
// engine 
		g2.setColor(Color.orange);			
		x = 1172;
		y = 10;
		width = 293;
		height = 109;
		g2.drawRoundRect(x, y, width, height, 10, 10);	
		g2.setFont(font3);
    	textWidth = fm.stringWidth("ENGINE");
    	textHeight = fm.getHeight();
    	x_text = (width - textWidth) / 2 + x; 
    	y_text = (height - textHeight) / 2 + fm.getAscent() + y;
	    g2.drawString("ENGINE", x_text, y+20);	
		
/* // left tires
		g2.setColor(Color.magenta);
		x = 270;
		y = 108;			
		g2.drawRoundRect(265, 103, 195, 212, 10, 10);
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
	    g2.drawString("RR", x_text, y+20); */

// speed
		g2.setColor(ISC);					
		g2.setFont(font);
		FontMetrics fm2 = g.getFontMetrics();
		x = 698;
		y = 130;
		width = 467;
		height = 254;
		g2.drawRoundRect(x, y, width, height, 10, 10);
    	textWidth = fm2.stringWidth("SPEED"); 
    	textHeight = fm2.getHeight();
    	x_text = (width - textWidth) / 2 + x; 
    	y_text = (height - textHeight) / 2 + fm2.getAscent() + y;
	    g2.drawString("SPEED", x_text, y+40);	

// right tyres	
/* 		g2.setColor(Color.magenta);			
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
	    g2.drawString("RR", x_text, y+20); */

// SoC
		int percentage = 10;

		g2.setColor(ISC);
		x = 398;
		y = 395;
		width = 1068;
		height = 72;			
		g2.drawRoundRect(x, y, width, height, 10, 10);
		g2.fillRoundRect(x, y, width * percentage / 100, height, 10, 10);
		g2.setColor(Color.white);
		g2.setFont(font2);
		x_text = (width - textWidth) / 2 + x; 
		y_text = y + height/2 + fm.getHeight();

		g2.drawString(percentage + "%", x_text, y_text);   

// brake

		percentage = 70;

		g2.setColor(Color.red);
		x = 1575;
		y = 40;
		width = 90;
		height = 400;	
		g2.drawRoundRect(x, y, width, height, 10, 10);
		g2.fillRoundRect(x, y + height * (100 - percentage) / 100, width, height * percentage / 100, 10, 10);
		g2.setColor(Color.white);
		g2.setFont(font4);
		x_text = x + width/4;
		y_text = y + height / 2 + fm.getAscent() - textHeight / 2;
		g2.drawString(percentage + "%", x_text, y_text);	

// throttle

		percentage = 33;
		g2.setColor(Color.green);	
		x = 1725;
		y = 40;
		width = 90;
		height = 400;
		g2.drawRoundRect(x, y, width, height, 10, 10);
		g2.fillRoundRect(x, y + height*(100-percentage)/100, width, height*percentage/100, 10, 10);
		g2.setColor(Color.white);
		g2.setFont(font4);
		x_text = x + width/4;
		y_text = y + height / 2 + fm.getAscent() - textHeight / 2;
		g2.drawString(percentage + "%", x_text, y_text);	

	}
}

