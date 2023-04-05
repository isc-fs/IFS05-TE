import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.12

Window {
    id: gameWindow
    width: 640
    height: 480
    title: "Pong"

    Rectangle {
        id: ball
        x: gameWindow.width / 2 - width / 2
        y: gameWindow.height / 2 - height / 2
        width: 20
        height: 20
        color: "white"

        property real dx: 5
        property real dy: 5

        function reset() {
            x = gameWindow.width / 2 - width / 2
            y = gameWindow.height / 2 - height / 2
            dx = 5
            dy = 5
        }

        function move() {
            x += dx
            y += dy

            if (y < 0 || y > gameWindow.height - height) {
                dy = -dy
            }

            if (x < 0) {
                dx = -dx
                player2Score.score++
                reset()
            }

            if (x > gameWindow.width - width) {
                dx = -dx
                player1Score.score++
                reset()
            }

            if (player1.contains(ball.x, ball.y) ||
                    player2.contains(ball.x + ball.width, ball.y)) {
                dx = -dx
            }
        }
    }

    Rectangle {
        id: player1
        x: 10
        y: gameWindow.height / 2 - height / 2
        width: 10
        height: 60
        color: "white"

        Keys.onPressed: {
            if (event.key === Qt.Key_W) {
                y -= 10
            }

            if (event.key === Qt.Key_S) {
                y += 10
            }
        }
    }

    Rectangle {
        id: player2
        x: gameWindow.width - width - 10
        y: gameWindow.height / 2 - height / 2
        width: 10
        height: 60
        color: "white"

        Keys.onPressed: {
            if (event.key === Qt.Key_Up) {
                y -= 10
            }

            if (event.key === Qt.Key_Down) {
                y += 10
            }
        }
    }

    Rectangle {
        id: divider
        x: gameWindow.width / 2 - width / 2
        y: 0
        width: 2
        height: gameWindow.height
        color: "white"
    }

    Text {
        id: player1Score
        x: gameWindow.width / 2 - 30
        y: 30
        text: "0"
        font.pixelSize: 30
        color: "white"

        property int score: 0
        onScoreChanged: {
            text = score
        }
    }

    Text {
        id: player2Score
        x: gameWindow.width / 2 + 10
        y: 30
        text: "0"
        font.pixelSize: 30
        color: "white"

        property int score: 0
        onScoreChanged: {
            text = score
        }
    }

    Timer {
        id: gameTimer
        interval: 10
        running: true
        repeat: true
        onTriggered: {
            ball.move()
        }
    }
}
