import QtQuick 2.15

Rectangle {
    id: inverter
    width: 195*1.5
    height: 91
    radius: 10
    color: "transparent"
    border.color: "orange"
    border.width: 1

    Text {
        text: "INVERTER"
        font.family: "Helvetica SemiBold"
        font.pixelSize: 13
        color: "white"
        font.bold: true
        anchors.top: parent.top
        anchors.horizontalCenter: parent.horizontalCenter
        topPadding: 10 // add padding from the top edge
    }
}
