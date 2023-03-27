import QtQuick 2.15

Item {
    width: 195*1.5
    height: 212

    Rectangle {
        anchors.fill: parent
        color: "transparent"
        border.color: "magenta"
        border.width: 1
        radius: 10

    }

    Rectangle {
        x: 7.5
        y: 5
        width: 185*1.5
        height: 99
        color: "transparent"
        radius: 10
        border.width: 2
        border.color: "magenta"
        Text {
            text: "FL"
            font.family: "Helvetica SemiBold"
            font.pointSize: 13
            font.bold: true
            color: "white"
            anchors.top: parent.top
            anchors.horizontalCenter: parent.horizontalCenter
            topPadding: 10
        }
    }

    Rectangle {
        x: 7.5
        y: 108
        width: 185*1.5
        height: 99
        color: "transparent"
        radius: 10
        border.width: 2
        border.color: "magenta"
        Text {
            text: "RL"
            font.family: "Helvetica SemiBold"
            font.pointSize: 13
            font.bold: true
            color: "white"
            anchors.top: parent.top
            anchors.horizontalCenter: parent.horizontalCenter
            topPadding: 10


        }
    }
}
