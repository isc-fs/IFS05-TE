import QtQuick 2.15

Rectangle {
    id: soc
    width: 712 * 1.5
    height: 60
    color: "transparent"
    border.color: "#FBBB1C"
    border.width: 1
    radius: 10

    property real percentage: 30

    Rectangle {
        id: filledArea
        x: 0
        y: 0
        width: soc.width * (percentage / 100)
        height: 60
        color: "#FBBB1C"
        radius: 10
    }

    Text {
        id: percentageText
        text: Math.round(percentage) + "%"
        font.family: "Helvetica SemiBold"
        font.pixelSize: 50
        color: "white"
        anchors.horizontalCenter: soc.horizontalCenter
        anchors.verticalCenter: soc.verticalCenter
    }

    Timer {
        interval: 1000
        running: true
        repeat: true
        onTriggered: {
            if (percentage <= 0) {
                percentage = 100;
            } else {
                percentage -= 1;
            }
        }
    }
}

