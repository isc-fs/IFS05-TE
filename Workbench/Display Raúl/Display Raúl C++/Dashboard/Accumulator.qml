import QtQuick 2.15

Rectangle {
    id: accumulator
    width: 311*1.5
    height: 91
    color: "transparent"
    border.color: "green"
    border.width: 1
    radius: 10

    Text {
        text: "ACCUMULATOR"
        font.family: "Helvetica SemiBold"
        font.pixelSize: 13
        color: "white"
        font.bold: true
        anchors.top: parent.top
        anchors.horizontalCenter: parent.horizontalCenter
        topPadding: 10 // add padding from the top edge
    }
}
