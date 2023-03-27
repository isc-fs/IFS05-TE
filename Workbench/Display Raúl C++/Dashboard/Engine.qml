import QtQuick 2.15

Rectangle {
    id: engine
    width: 195*1.5
    height: 91
    color: "transparent"
    border.color: "orange"
    border.width: 1
    radius: 10

    Text {
        text: "ENGINE"
        font.family: "Helvetica SemiBold"
        font.pixelSize: 13
        color: "white"
        font.bold: true
        anchors.top: parent.top
        anchors.horizontalCenter: parent.horizontalCenter
        topPadding: 10 // add padding from the top edge
    }
}
