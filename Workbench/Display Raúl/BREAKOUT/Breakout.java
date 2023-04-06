import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Rectangle;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class Breakout extends JPanel implements KeyListener {
    private int paddleX = 250;
    private int ballX = 290;
    private int ballY = 460;
    private int ballXSpeed = 3;
    private int ballYSpeed = -3;
    private int lives = 3;
    private int score = 0;
    private int level = 1;
    private boolean gameOver = false;
    private boolean gameWon = false;
    private List<Rectangle> bricks = new ArrayList<>();

    public Breakout() {
        addKeyListener(this);
        setFocusable(true);
        setFocusTraversalKeysEnabled(false);
        createBricks();
    }

    public void paint(Graphics g) {
        // Draw the game board
        g.setColor(Color.BLACK);
        g.fillRect(0, 0, 600, 500);

        // Draw the paddle
        g.setColor(Color.WHITE);
        g.fillRect(paddleX, 470, 100, 10);

        // Draw the ball
        g.setColor(Color.RED);
        g.fillOval(ballX, ballY, 20, 20);

        // Draw the bricks
        for (Rectangle brick : bricks) {
            g.setColor(Color.BLUE);
            g.fillRect(brick.x, brick.y, brick.width, brick.height);
        }

        // Draw the lives and score
        g.setColor(Color.WHITE);
        g.setFont(new Font("Arial", Font.PLAIN, 20));
        g.drawString("Lives: " + lives, 10, 25);
        g.drawString("Score: " + score, 500, 25);

        // Check for collision with the paddle
        if (new Rectangle(ballX, ballY, 20, 20).intersects(new Rectangle(paddleX, 470, 100, 10))) {
            ballYSpeed = -ballYSpeed;
        }

        // Check for collision with the bricks
        for (Rectangle brick : bricks) {
            if (new Rectangle(ballX, ballY, 20, 20).intersects(brick)) {
                bricks.remove(brick);
                score += 10;
                ballYSpeed = -ballYSpeed;
                break;
            }
        }

        // Check for collision with the game board edges
        if (ballX < 0 || ballX > 580) {
            ballXSpeed = -ballXSpeed;
        }
        if (ballY < 0) {
            ballYSpeed = -ballYSpeed;
        }
        if (ballY > 470) {
            lives--;
            if (lives == 0) {
                gameOver = true;
            } else {
                ballX = 290;
                ballY = 460;
                ballXSpeed = 3;
                ballYSpeed = -3;
                paddleX = 250;
            }
        }

        // Check if all the bricks have been destroyed
        if (bricks.isEmpty()) {
            if (level == 3) {
                gameWon = true;
            } else {
                level++;
                createBricks();
                ballX = 290;
                ballY = 460;
                ballXSpeed = 3;
                ballYSpeed = -3;
                paddleX = 250;
            }
        }

