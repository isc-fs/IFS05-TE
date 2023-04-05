import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Font;
import java.awt.FontMetrics;

import javax.swing.JPanel;

public class GamePanel extends JPanel implements Runnable {
    Thread gameThread;

    private boolean showRectangle = true;

    Color fondo = new Color(25, 26, 30);
    Color ISC = new Color(251, 187, 28);
    Color ISCgreen = new Color(92, 132, 28);

    Font font = new Font("Helvetica SemiBold", Font.BOLD, 40);
    Font font2 = new Font("Helvetica SemiBold", Font.BOLD, 57);
    Font font3 = new Font("Helvetica SemiBold", Font.BOLD, 13);
    Font font4 = new Font("Helvetica SemiBold", Font.BOLD, 30);

    public GamePanel() {
        this.setPreferredSize(new Dimension(1920, 480));
        this.setBackground(fondo);
        this.setDoubleBuffered(true);
    }

    public void startGameThread() {
        gameThread = new Thread(this);
        gameThread.start();
    }

    @Override
    public void run() {
        while (gameThread != null) {
            // 1. Update
            update();

            // 2. Draw
            repaint();
        }
    }

    public void update() {
        try {
            Thread.sleep(500);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        showRectangle = !showRectangle;
    }

    public void paintComponent(Graphics g) {
        super.paintComponent(g);

        Graphics2D g2 = (Graphics2D) g;

        // warnings
        int x1 = 60;
        int y1 = 130;
        if (showRectangle) {
            g2.setColor(Color.red);
            g2.fillRoundRect(x1, y1, 185, 212, 10, 10);
            g2.drawRoundRect(50, 120, 205, 232, 10, 10);
            g2.setColor(Color.white);
            g2.setFont(font4);
            FontMetrics fm1 = g.getFontMetrics();
            int textWidth1 = fm1.stringWidth("WARNING");
            int textHeight1 = fm1.getHeight();
            int x_text1 = (185 - textWidth1) / 2 + x1;
            int y_text1 = (212 - textHeight1) / 2 + fm1.getAscent() + y1;
            g2.drawString("WARNING", x_text1, y_text1);
        }

        // inversor
        int x = 350;
        int y = 10;
        g2.setColor(Color.orange);
        g2.drawRoundRect(x, y, 195, 91, 10, 10);
        g2.setFont(font3);
        FontMetrics fm = g.getFontMetrics();
        int textWidth = fm.stringWidth("INVERSOR");
        int textHeight = fm.getHeight();
        int x_text = (195 - textWidth) / 2 + x;
        int y_text = (91 - textHeight) / 2 + fm.getAscent() + y;
        g2.drawString("INVERSOR", x_text, y + 20);  

		// batteries
		g2.setColor(Color.green);			
		x = 600;
		y = 10; 
		g2.drawRoundRect(x, y, 311, 91, 10, 10);	
		g2.setFont(font3);	
    	textWidth = fm.stringWidth("BATTERIES");
    	textHeight = fm.getHeight();
        x_text = (311 - textWidth) / 2 + x;
        y_text = (91 - textHeight) / 2 + fm.getAscent() + y;
        g2.drawString("BATTERIES", x_text, y + 20);

        // engine
        x = 1000;
        y = 10;
        g2.setColor(Color.orange);
        g2.drawRoundRect(x, y, 195, 91, 10, 10);
        g2.setFont(font3);
        textWidth = fm.stringWidth("ENGINE");
        x_text = (195 - textWidth) / 2 + x;
        y_text = (91 - textHeight) / 2 + fm.getAscent() + y;
        g2.drawString("ENGINE", x_text, y + 20);	
		
        // left tires
        g2.setColor(Color.magenta);
        x = 350;
        y = 130;
        g2.drawRoundRect(x, y, 195, 212, 10, 10);
        g2.setFont(font3);

        y = 140;
        textWidth = fm.stringWidth("FL");
        x_text = (195 - textWidth) / 2 + x;
        y_text = (99 - textHeight) / 2 + fm.getAscent() + y;
        g2.drawString("FL", x_text, y_text);

        y = 244;
        textWidth = fm.stringWidth("RL");
        x_text = (195 - textWidth) / 2 + x;
        y_text = (99 - textHeight) / 2 + fm.getAscent() + y;
        g2.drawString("RL", x_text, y_text);

        // speed
        g2.setColor(ISC);
        x = 600;
        y = 130;
        g2.drawRoundRect(x, y, 311, 212, 10, 10);
        g2.setFont(font);
        FontMetrics fm2 = g.getFontMetrics();
        textWidth = fm2.stringWidth("SPEED");
        int textHeight2 = fm2.getHeight();
        x_text = (311 - textWidth) / 2 + x;
        y_text = (212 - textHeight2) / 2 + fm2.getAscent() + y;
        g2.drawString("SPEED", x_text, y + 40);

        // right tires
        g2.setColor(Color.blue);
        x = 1000;
        y = 130;
        g2.drawRoundRect(x, y, 195, 212, 10, 10);
        g2.setFont(font3);

        y = 140;
        textWidth = fm.stringWidth("FR");
        x_text = (195 - textWidth) / 2 + x;
        y_text = (99 - textHeight) / 2 + fm.getAscent() + y;
        g2.drawString("FR", x_text, y_text);

        y = 244;
        textWidth = fm.stringWidth("RR");
        x_text = (195 - textWidth) / 2 + x;
        y_text = (99 - textHeight) / 2 + fm.getAscent() + y;
        g2.drawString("RR", x_text, y_text);

        // SOC (State of Charge)
        g2.setColor(Color.cyan);
        x = 1250;
        y = 10;
        g2.drawRoundRect(x, y, 195, 91, 10, 10);
        g2.setFont(font3);
        textWidth = fm.stringWidth("SOC");
        x_text = (195 - textWidth) / 2 + x;
        y_text = (91 - textHeight) / 2 + fm.getAscent() + y;
        g2.drawString("SOC", x_text, y + 20);
  

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

