import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Pong extends JPanel implements KeyListener, ActionListener {
    // Constants for game dimensions and speed
    private final int WIDTH = 1920;
    private final int HEIGHT = 480;
    private final int PADDLE_WIDTH = 10;
    private final int PADDLE_HEIGHT = 80;
    private final int BALL_SIZE = 20;
    private final int PADDLE_SPEED = 5;
    private final int BALL_SPEED = 5;
    private final int DELAY = 10;
    
    // Variables for game objects
    private int paddle1Y = HEIGHT/2 - PADDLE_HEIGHT/2;
    private int paddle2Y = HEIGHT/2 - PADDLE_HEIGHT/2;
    private int ballX = WIDTH/2 - BALL_SIZE/2;
    private int ballY = HEIGHT/2 - BALL_SIZE/2;
    private int ballXSpeed = BALL_SPEED;
    private int ballYSpeed = BALL_SPEED;
    
    // Variables for game state
    private boolean gameStarted = false;
    private boolean gameOver = false;
    private int player1Score = 0;
    private int player2Score = 0;
    
    // Timer for game loop
    private Timer timer;
    
    // Constructor
    public Pong() {
        // Set up window and game objects
        setPreferredSize(new Dimension(WIDTH, HEIGHT));
        setBackground(Color.BLACK);
        setFocusable(true);
        addKeyListener(this);
        timer = new Timer(DELAY, this);
        timer.start();
    }
    
    // Method for drawing game objects
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        
        // Draw paddles and ball
        g.setColor(Color.WHITE);
        g.fillRect(0, paddle1Y, PADDLE_WIDTH, PADDLE_HEIGHT);
        g.fillRect(WIDTH - PADDLE_WIDTH, paddle2Y, PADDLE_WIDTH, PADDLE_HEIGHT);
        g.fillOval(ballX, ballY, BALL_SIZE, BALL_SIZE);
        
        // Draw scores
        g.setFont(new Font("Arial", Font.BOLD, 50));
        g.drawString(Integer.toString(player1Score), WIDTH/4, 50);
        g.drawString(Integer.toString(player2Score), WIDTH*3/4, 50);
        
        // Draw game over message if game is over
        if (gameOver) {
            g.setFont(new Font("Arial", Font.BOLD, 100));
            g.drawString("Game Over", WIDTH/2 - 250, HEIGHT/2 - 50);
        }
    }
    
    // Method for updating game state
    public void actionPerformed(ActionEvent e) {
        if (gameStarted && !gameOver) {
            // Move ball
            ballX += ballXSpeed;
            ballY += ballYSpeed;
            
            // Check for collision with paddles
            if (ballX <= PADDLE_WIDTH && ballY >= paddle1Y && ballY <= paddle1Y + PADDLE_HEIGHT) {
                ballXSpeed = BALL_SPEED;
            } else if (ballX + BALL_SIZE >= WIDTH - PADDLE_WIDTH && ballY >= paddle2Y && ballY <= paddle2Y + PADDLE_HEIGHT) {
                ballXSpeed = -BALL_SPEED;
            }
            
            // Check for collision with walls
            if (ballY <= 0 || ballY + BALL_SIZE >= HEIGHT){
                ballYSpeed = -ballYSpeed;
                }
                        // Check for scoring
        if (ballX <= 0) {
            player2Score++;
            resetBall();
        } else if (ballX + BALL_SIZE >= WIDTH) {
            player1Score++;
            resetBall();
        }
        
        // Move paddles
        movePaddles();
    }
    
    // Redraw screen
    repaint();
}

// Method for moving paddles based on key input
public void keyPressed(KeyEvent e) {
    int key = e.getKeyCode();
    
    if (key == KeyEvent.VK_UP) {
        paddle2Y -= PADDLE_SPEED;
    } else if (key == KeyEvent.VK_DOWN) {
        paddle2Y += PADDLE_SPEED;
    } else if (key == KeyEvent.VK_W) {
        paddle1Y -= PADDLE_SPEED;
    } else if (key == KeyEvent.VK_S) {
        paddle1Y += PADDLE_SPEED;
    }
}

public void keyTyped(KeyEvent e) {}
public void keyReleased(KeyEvent e) {}

// Method for moving computer paddle
private void movePaddles() {
    // Move player 1 paddle
    if (paddle1Y + PADDLE_HEIGHT/2 < ballY) {
        paddle1Y += PADDLE_SPEED;
    } else if (paddle1Y + PADDLE_HEIGHT/2 > ballY) {
        paddle1Y -= PADDLE_SPEED;
    }
    
    // Move player 2 paddle
    if (paddle2Y + PADDLE_HEIGHT/2 < ballY) {
        paddle2Y += PADDLE_SPEED;
    } else if (paddle2Y + PADDLE_HEIGHT/2 > ballY) {
        paddle2Y -= PADDLE_SPEED;
    }
}

// Method for resetting ball to center of screen
private void resetBall() {
    ballX = WIDTH/2 - BALL_SIZE/2;
    ballY = HEIGHT/2 - BALL_SIZE/2;
    ballXSpeed = BALL_SPEED;
    ballYSpeed = BALL_SPEED;
    gameStarted = false;
    timer.stop();
    
    // Check for game over
    if (player1Score == 10 || player2Score == 10) {
        gameOver = true;
    }
}

// Main method
public static void main(String[] args) {
    JFrame frame = new JFrame("Pong");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setResizable(false);
    Pong pong = new Pong();
    frame.getContentPane().add(pong);
    frame.pack();
    frame.setVisible(true);
}

}



