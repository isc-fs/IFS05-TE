import QtQuick 2.15

Rectangle {
    id: brake
    width: 80
    height: 320
    color: "transparent"
    border.color: "red"
    border.width: 1
    radius: 10

    property real percentage: 70

    Rectangle {
        id: brakePercentage
        x: 0
        y: brake.height - brake.height * (percentage / 100)
        width: 80
        height: brake.height * (percentage / 100)
        color: "red"
        radius: 10
    }

    Text {
        x: 0
        y: 160
        text: Math.round(percentage) + "%"
        font.family: "Helvetica SemiBold"
        font.pixelSize: 30
        color: "white"
        anchors.centerIn: brakePercentage
    }
}
