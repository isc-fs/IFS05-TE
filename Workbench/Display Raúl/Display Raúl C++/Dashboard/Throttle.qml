import QtQuick 2.15

Rectangle {
    id: throttle
    width: 80
    height: 320
    color: "transparent"
    border.color: "green"
    border.width: 1
    radius: 10

    property real percentage: 95

    Rectangle {
        id: throttlePercentage
        x: 0
        y: parent.height - parent.height * (percentage / 100)
        width: 80
        height: parent.height * (percentage / 100)
        color: "green"
        radius: 10
    }

    Text {
        x: 0
        y: 160
        text: percentage.toFixed(0) + "%"
        font.family: "Helvetica SemiBold"
        font.pixelSize: 30
        color: "white"
        anchors.centerIn: throttlePercentage
    }
}
